# Deployment & Infrastructure

[← Back to Main Page](../../index.md)

This page documents how Educado actually runs in the deployed environment: the topology, the build strategies, the
domains, and the complete table of environment variables.

For the local development setup see the [Back End Getting Started](../../handbook/back-end/getting-started.md) and the
[Web Getting Started](../../handbook/web/getting-started.md) guides.

## Topology

Everything runs on a single VPS managed by **Coolify 4.3.1**, a self hosted PaaS. Coolify provisions the containers,
manages the environment variables and configures **Traefik** as the reverse proxy, which terminates TLS and routes the
public hostnames to the right container.

```text
                Internet
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

    MinIO was removed from the Coolify service catalog in 4.3.1, so it cannot be added as a one click resource. It is
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
| `PORT`                | Yes                 | Port the Express server listens on. Defaults to `5000` if unset.                               |
| `POSTGRES_URI`        | Yes (production)    | PostgreSQL connection string. Read **only** when `NODE_ENV === 'production'`.                 |
| `POSTGRES_URI_DEV`    | Yes (non production) | Connection string used whenever `NODE_ENV` is not `production`.                              |
| `ACCESS_TOKEN_SECRET` | Yes                 | Secret used to sign and verify JWTs. Generate with `openssl rand -base64 48`.                  |
| `FRONTEND_ORIGIN`     | Yes (production)    | Comma separated CORS allowlist, for example `https://educado.tominho.com`.                     |
| `S3_ENDPOINT`         | Yes                 | MinIO/S3 endpoint URL.                                                                          |
| `S3_REGION`           | Yes                 | Region string, for example `us-east-1`.                                                        |
| `S3_ACCESS_KEY`       | Yes                 | Object storage access key.                                                                      |
| `S3_SECRET_KEY`       | Yes                 | Object storage secret key.                                                                      |
| `S3_BUCKET`           | Yes                 | Bucket holding media assets, for example `educado-media`.                                      |
| `EMAIL_API_KEY`       | Yes                 | Resend API key. Without it the worker cannot deliver.                                           |
| `EMAIL_FROM`          | Yes                 | Sender address used on transactional email.                                                     |
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

!!! warning "Redis with a password"

    `REDIS_PASSWORD` has no default. When the Redis resource requires authentication and the variable is missing,
    BullMQ connects but every command is rejected, so email jobs are enqueued and never delivered.

!!! note "Schema changes in production"

    In production `sequelize.sync()` runs without `alter`, so new columns are not created automatically. Structural
    changes must be applied deliberately before the deploy that depends on them.

## Deploy checklist

1. Confirm `NODE_ENV=production` on both the API and the worker.
2. Confirm `POSTGRES_URI`, `REDIS_HOST`, `REDIS_PORT` and `REDIS_PASSWORD` point at the Coolify resources.
3. Confirm the S3 variables point at MinIO and that the bucket exists.
4. Confirm `FRONTEND_ORIGIN` contains the deployed web origin, otherwise the browser blocks every request.
5. For the web app, confirm `VITE_API_URL` is set as a **build argument** and trigger a rebuild after changing it.
6. After deploying, check [https://api-educado.tominho.com/docs/](https://api-educado.tominho.com/docs/) and load the
   web app once to validate the API URL that was compiled into the bundle.

[← Back to Main Page](../../index.md)
