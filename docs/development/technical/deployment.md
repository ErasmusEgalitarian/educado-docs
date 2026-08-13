# Deployment & Infrastructure

[← Back to Main Page](../../index.md)

This page documents how Educado actually runs in the deployed environment: the topology, the build strategies, the
domains, and the environment variables read by the code. The variable table below is kept in sync with the
`process.env` reads in `educado-api/src`; when a new one is introduced, add it here in the same commit.

For the local development setup see the [Back End Getting Started](../../handbook/back-end/getting-started.md) and the
[Web Getting Started](../../handbook/web/getting-started.md) guides.

## Topology

Everything runs on a single VPS managed by **Coolify 4.3.1** (version observed in the panel on 2026-08-13), a self
hosted PaaS. Coolify provisions the containers, manages the environment variables and configures **Traefik** as the
reverse proxy, which terminates TLS and routes the public hostnames to the right container. Public traffic does not
reach Traefik directly: a **Cloudflare Tunnel** sits in front of the VPS, so Cloudflare is the first hop for every
request.

```text
                Internet
                    |
              +-----v-------------+
              | Cloudflare        |  DNS, TLS at the edge, Tunnel to the VPS
              | (Tunnel, Free)    |  request body limit: 100 MB
              +-----+-------------+
                    |
                 (443/tcp)
                    |
              +-----v------+
              |  Traefik   |  TLS termination, routing (managed by Coolify)
              +--+------+--+
                 |      |
   educado.tominho.com  api-educado.tominho.com
                 |      |
       +---------v+    +v-----------------+
       | web      |    | api (Express)    |
       | nginx    |    | node build/index.js
       +----------+    +--+-------+-------+
                          |       |
                          |       +-------------------+
              +-----------v--+  +-v---------+  +------v------+
              | PostgreSQL 16|  | Redis 7.2 |  | MinIO (S3)  |
              +--------------+  +-----+-----+  +-------------+
                                      |
                              +-------v----------+
                              | email worker     |
                              | node build/workers/email-worker.js
                              +------------------+
```

All application containers share the internal Coolify Docker network, so the API reaches PostgreSQL, Redis and MinIO by
service name. Only Traefik publishes ports to the internet: the databases and the object storage are never exposed
directly.

!!! warning "Cloudflare caps the request body at 100 MB"

    On the Cloudflare Free plan the maximum request body size is **100 MB**, and that ceiling applies to every
    request that crosses the tunnel, including media uploads. The API code accounts for it explicitly: the comment
    above the legacy direct upload route in `src/routes/media/upload-video.ts` (lines 30-31) marks the endpoint as
    "subject to the reverse-proxy body limit (Cloudflare Free = 100 MB)".

    This is why video upload uses the **chunked flow** (`/media/videos/init`,
    `/media/videos/:id/parts/:partNumber`, `/media/videos/:id/complete`): each part is bounded by the client side
    chunk size of 50 MB, comfortably below the ceiling. The legacy `POST /media/videos` route uploads the whole file
    in one request, so anything above 100 MB is rejected at the edge, before the API ever sees it. A failed large
    upload with no trace in the API logs is the signature of this limit.

## Domains

| Component  | Hostname                                                                        |
| ---------- | ------------------------------------------------------------------------------- |
| Web app    | [https://educado.tominho.com](https://educado.tominho.com)                      |
| API        | [https://api-educado.tominho.com](https://api-educado.tominho.com)              |
| Swagger UI | [https://api-educado.tominho.com/docs/](https://api-educado.tominho.com/docs/)  |

## Deployed components

| Component     | Build strategy | Start command                          | Notes                                                          |
| ------------- | -------------- | -------------------------------------- | -------------------------------------------------------------- |
| API           | Nixpacks       | `node build/index.js`                | Express server plus Swagger UI.                                |
| Email worker  | Nixpacks       | `node build/workers/email-worker.js` | Same repository and build, separate process. No public domain.  |
| Web           | Dockerfile     | `nginx -g "daemon off;"`             | Multi stage build: Node 20 builds, nginx serves `/dist`.     |
| PostgreSQL 16 | Coolify resource | managed                              | Persistent volume.                                             |
| Redis 7.2     | Coolify resource | managed                              | Password protected.                                            |
| MinIO         | Docker Compose | managed                                | See the caveat below.                                          |

!!! warning "MinIO is not in the Coolify 4.3.1 catalog"

    MinIO was removed from the Coolify service catalog in 4.3.1, so it cannot be added as a one click resource
    (observed in the Coolify panel on 2026-08-13; re-check when the instance is upgraded). It is
    deployed as a **Docker Compose** resource inside Coolify instead. When rebuilding the environment from scratch,
    do not look for it in the service list: create a Compose resource with the MinIO image, attach a persistent volume
    and create the media bucket before pointing the API at it.

### Web build argument

The web application is a static bundle, so the API URL is baked in **at build time**, not at runtime. The Dockerfile
declares:

```dockerfile
ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}
RUN npm run build
```

`VITE_API_URL` must be set as a **build argument** in Coolify (value: `https://api-educado.tominho.com`). Setting
it only as a runtime environment variable has no effect: the bundle will fall back to `http://localhost:5001` and the
deployed site will fail to reach the API. Changing the API URL requires a rebuild, not a restart.

nginx serves the bundle with an SPA fallback (`try_files $uri $uri/ /index.html`) and long lived cache headers for
hashed assets.

## Environment variables

### API and email worker

Both processes are built from the same repository and take the same variables.

| Variable                | Required            | Description                                                                                     |
| ----------------------- | ------------------- | ------------------------------------------------------------------------------------------------ |
| `NODE_ENV`            | Yes                 | Must be exactly `production` in the deployed environment. See the trap below.                  |
| `PORT`                | No                  | Port the Express server listens on. Defaults to `5000` when unset (`src/index.ts:41`).       |
| `POSTGRES_URI`        | Yes (production)    | PostgreSQL connection string. Read **only** when `NODE_ENV === 'production'`.                 |
| `POSTGRES_URI_DEV`    | Yes (non production) | Connection string used whenever `NODE_ENV` is not `production`.                              |
| `ACCESS_TOKEN_SECRET` | Yes                 | Secret used to sign and verify JWTs. Generate with `openssl rand -base64 48`.                  |
| `JWT_SECRET`          | No (alias)          | Accepted alias of `ACCESS_TOKEN_SECRET`, read in `src/config/jwt.ts:7` as `process.env.ACCESS_TOKEN_SECRET ?? process.env.JWT_SECRET`. `ACCESS_TOKEN_SECRET` wins when both are set. Set one, not both. |
| `FRONTEND_ORIGIN`     | Yes (production)    | Comma separated CORS allowlist, for example `https://educado.tominho.com`.                     |
| `S3_ENDPOINTS`        | No, but it overrides `S3_ENDPOINT` | Comma separated list of S3/MinIO endpoints, tried in order. **Takes precedence over `S3_ENDPOINT`.** See the trap below. |
| `S3_ENDPOINT`         | Yes, unless `S3_ENDPOINTS` is set | Single MinIO/S3 endpoint URL. Ignored whenever `S3_ENDPOINTS` is set and non empty. Defaults to `http://localhost:9000`. |
| `S3_REGION`           | Yes                 | Region string, for example `us-east-1`. Defaults to `us-east-1`.                              |
| `S3_ACCESS_KEY`       | Yes                 | Object storage access key. Defaults to `minioadmin`.                                           |
| `S3_SECRET_KEY`       | Yes                 | Object storage secret key. Defaults to `minioadmin`.                                           |
| `S3_BUCKET`           | Yes                 | Bucket holding media assets, for example `educado-media`.                                      |
| `S3_MAX_ATTEMPTS`     | No                  | How many times each endpoint is retried on a transient network error (`EAI_AGAIN`, `ENOTFOUND`, `ECONNRESET`, `ETIMEDOUT`). Defaults to `3`. Values below 1 or unparseable fall back to the default. |
| `S3_RETRY_DELAY_MS`   | No                  | Delay in milliseconds between those retries. Defaults to `150`. Same fallback rule as above.  |
| `EMAIL_API_KEY`       | Yes                 | Resend API key. Without it the worker cannot deliver.                                           |
| `EMAIL_FROM`          | Yes                 | Sender address used on transactional email.                                                     |
| `SYSTEM_REVIEWER_EMAIL` | No                | Identity recorded as the reviewer when a creator registration is auto approved by verified email domain (`AUTO_EMAIL_DOMAIN_VERIFIED`). Read in `src/application/verification/email-verification-service.ts:22`. Defaults to `system@educado.local`, an address that does not resolve, so set a real mailbox if the audit trail matters. |
| `CERTIFICATE_VERIFICATION_URL` | Yes (production) | Base URL printed on every issued certificate PDF. See the trap below: the built in default points outside the project. |
| `REDIS_HOST`          | Yes                 | Redis hostname. Defaults to `127.0.0.1` if unset, which is wrong in a container.               |
| `REDIS_PORT`          | Yes                 | Redis port. Defaults to `6379`.                                                                |
| `REDIS_PASSWORD`      | Yes, when Redis has a password | Read in `src/infrastructure/queue/redis.ts`. Omitting it makes every queue operation fail with `NOAUTH`. |

### Web

| Variable         | Scope           | Description                                                                        |
| ---------------- | --------------- | ---------------------------------------------------------------------------------- |
| `VITE_API_URL` | **Build time** | Base URL of the API. Must be a Docker build argument, not a runtime variable.       |

## Operational traps

!!! danger "`NODE_ENV` must be exactly `production`"

    `src/config/database.ts` selects the connection string like this:

    ```ts
    const isProd = () => process.env.NODE_ENV === 'production'
    const postgresUri = isProd() ? process.env.POSTGRES_URI : process.env.POSTGRES_URI_DEV
    ```

    Any other value, including `staging`, makes the API look for `POSTGRES_URI_DEV`. In a deployed environment that
    variable does not exist, the connection fails, and the process exits with `process.exit(1)`, which the supervisor
    restarts, producing a crash loop. If the API is restarting endlessly right after a deploy, check `NODE_ENV`
    first.

    The same flag also drives HTTPS enforcement, CORS strictness and whether `sequelize.sync()` is allowed to alter
    tables, so the value is not cosmetic.

!!! danger "`S3_ENDPOINTS` silently overrides `S3_ENDPOINT`"

    The two variables look interchangeable and are not. `src/infrastructure/storage/s3/s3-client.ts:50` resolves the
    endpoint list like this:

    ```ts
    const rawEndpoints =
      process.env.S3_ENDPOINTS || process.env.S3_ENDPOINT || DEFAULT_S3_ENDPOINT
    ```

    `S3_ENDPOINTS` (**plural**) is read first. If it is set to anything non empty, `S3_ENDPOINT` (singular) is never
    read at all. Editing the singular variable to repoint storage while a stale plural one is still present in the
    Coolify environment changes nothing, and the failure looks like a caching or DNS problem rather than a
    configuration one. When storage points at the wrong place, check `S3_ENDPOINTS` **before** `S3_ENDPOINT`.

    The plural form takes a comma separated list. Entries are trimmed, empties are dropped and duplicates are
    removed, then each endpoint is tried in order, which is what makes it useful: an internal Docker hostname first,
    a public URL as fallback. Falling back to `http://localhost:9000` in a container is the symptom of both being
    unset.

!!! danger "`CERTIFICATE_VERIFICATION_URL` defaults to a domain the project does not own"

    `src/application/certificates/certificate-pdf-service.ts:8` falls back to a hardcoded value:

    ```ts
    const VERIFICATION_BASE_URL =
      process.env.CERTIFICATE_VERIFICATION_URL ||
      'https://educado.com/certificates/verify'
    ```

    `educado.com` is **not** a domain of this project. If the variable is not configured, every certificate issued in
    production is stamped with a verification link pointing at third party infrastructure, and nothing fails loudly:
    the PDF is generated, the student receives it, and the link only breaks when someone tries to verify it. Worse,
    already issued PDFs cannot be corrected after the fact.

    Set it explicitly on the API and the worker, and check it before the first certificate is issued in any new
    environment. The only verification surface that exists today is the public API route
    `GET /certificates/verify/:code`, so `https://api-educado.tominho.com/certificates/verify` is a value that
    actually resolves. There is no verification page in `educado-web` yet; once one exists, point the variable at it
    instead.

!!! warning "Redis with a password"

    `REDIS_PASSWORD` has no default. When the Redis resource requires authentication and the variable is missing,
    BullMQ connects but every command is rejected, so email jobs are enqueued and never delivered.

!!! note "Schema changes in production"

    In production `sequelize.sync()` runs without `alter`, so new columns are not created automatically. Structural
    changes must be applied deliberately before the deploy that depends on them.

## Deploy checklist

1. Confirm `NODE_ENV=production` on both the API and the worker.
2. Confirm `POSTGRES_URI`, `REDIS_HOST`, `REDIS_PORT` and `REDIS_PASSWORD` point at the Coolify resources.
3. Confirm the S3 variables point at MinIO and that the bucket exists. Check `S3_ENDPOINTS` first: when it is set it
   overrides `S3_ENDPOINT` entirely.
4. Confirm `CERTIFICATE_VERIFICATION_URL` is set, so certificates are not stamped with the `educado.com` default.
5. Confirm `FRONTEND_ORIGIN` contains the deployed web origin, otherwise the browser blocks every request.
6. For the web app, confirm `VITE_API_URL` is set as a **build argument** and trigger a rebuild after changing it.
7. After deploying, check [https://api-educado.tominho.com/docs/](https://api-educado.tominho.com/docs/) and load the
   web app once to validate the API URL that was compiled into the bundle.

[← Back to Main Page](../../index.md)
