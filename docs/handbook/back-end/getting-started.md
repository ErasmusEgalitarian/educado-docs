# Back End: Getting Started

This guide sets up `educado-api` for local development. The API is a Node.js 20 + Express 5 + TypeScript service
backed by PostgreSQL, Redis and MinIO.

For the deployed environment and the full environment variable reference, see
[Deployment & Infrastructure](../../development/technical/deployment.md). For the system design, see
[System Architecture](../../development/technical/architecture.md).

## Prerequisites

- **Node.js 20 or newer.** The project declares `engines.node >= 20`. Install it with
  [nvm](https://github.com/nvm-sh/nvm) (macOS/Linux) or [nvm-windows](https://github.com/coreybutler/nvm-windows).
- **Docker and the Compose plugin.** Required: the local database, cache and object storage all run in containers.
- **Git**, ideally with SSH authentication configured. See the
  [GitHub docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
- A REST client (Postman, Insomnia, `curl`) or just the built in Swagger UI.

## Clone the repository

```shell
git clone git@github.com:ErasmusEgalitarian/educado-api.git
cd educado-api
```

## Start the local infrastructure

```shell
docker compose up -d
```

!!! important

    Compose starts **only the infrastructure**, not the API. The services it brings up are:

    | Service        | Container              | Host port                        | Purpose                                  |
    | -------------- | ---------------------- | -------------------------------- | ---------------------------------------- |
    | `postgres`   | `educado-postgres`   | `5431` (container 5432)        | Database `educado_dev`                 |
    | `redis`      | `educado-redis`      | `6380` (container 6379)        | BullMQ queue backend                     |
    | `minio`      | `educado-minio`      | `9002` API, `9003` console   | S3 compatible object storage             |
    | `minio-setup` | `educado-minio-setup` | none                            | One shot job that creates the `educado-media` bucket and exits |

    The API itself runs on the host with `npm run dev`, and the email worker with `npm run worker:email`.

The `minio-setup` container is expected to exit after it finishes: a `Bucket educado-media ready` line in its logs
followed by `Exited (0)` means success, not a failure.

Default local credentials: PostgreSQL `educado` / `educado`, MinIO `minioadmin` / `minioadmin`. The MinIO
console is at [http://localhost:9003](http://localhost:9003).

To check the containers:

```shell
docker compose ps
docker compose logs -f postgres
```

## Install dependencies

```shell
npm install
```

Run it again whenever you switch branches or pull changes that touch `package.json` or `package-lock.json`.

## Environment variables

Copy the template and adjust it:

```shell
cp .env.example .env
```

A working local `.env` looks like this:

```dotenv
NODE_ENV=development
PORT=5001

POSTGRES_URI_DEV=postgresql://educado:educado@localhost:5431/educado_dev

FRONTEND_ORIGIN=http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173,http://127.0.0.1:5173
ACCESS_TOKEN_SECRET=replace-with-a-strong-secret

S3_ENDPOINT=http://localhost:9002
S3_REGION=us-east-1
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=educado-media

EMAIL_API_KEY=
EMAIL_FROM=noreply@example.com

REDIS_HOST=localhost
REDIS_PORT=6380
```

!!! warning "The ports in `.env.example` do not all match `docker-compose.yml`"

    `.env.example` ships with `S3_ENDPOINT=http://localhost:9000` and `REDIS_PORT=6379`, which are the
    **container** ports. Compose publishes them on the host as **9002** and **6380** to avoid clashing with other
    local services. Use the host ports in your `.env`, as shown above. PostgreSQL is already correct in the
    template (`5431`).

Generate a real secret with:

```shell
openssl rand -base64 48
```

Never commit `.env`.

## Run the API

```shell
npm run dev
```

The script forces `NODE_ENV=development` and runs `src/index.ts` through nodemon, so it reloads on save. On a
successful start you should see the PostgreSQL connection message followed by `Server is running on port: 5001`.

!!! warning "Windows: `npm run dev` does not work in cmd or PowerShell"

    The script is written as an inline environment assignment:

    ```json
    "dev": "NODE_ENV=development nodemon src/index.ts"
    ```

    That syntax is POSIX shell only. Windows `cmd` reports `'NODE_ENV' is not recognized as an internal or external
    command`, and PowerShell fails in its own way, because neither treats `VAR=value command` as an assignment.

    Work around it by running the project from **WSL** or **Git Bash**, which is the recommended setup, or by
    setting the variable separately for the session and calling nodemon directly:

    ```powershell
    $env:NODE_ENV = "development"; npx nodemon src/index.ts
    ```

    Do not "fix" this by dropping `NODE_ENV`: without it the API falls back to the non production branch anyway, but
    other scripts and the deployed environment rely on the value being explicit.

Then open the interactive contract at [http://localhost:5001/docs/](http://localhost:5001/docs/). Swagger is the
canonical description of every request and response shape.

In development `sequelize.sync()` runs with `alter: true`, so model changes are reflected in the local database on
restart. There is no separate migration step.

### Seed data

To populate the database with sample courses:

```shell
npm run seed
```

## Run the email worker

Email delivery is asynchronous: use cases enqueue jobs on a BullMQ queue backed by Redis, and a separate process sends
them through Resend. In a second terminal:

```shell
npm run worker:email
```

It prints `Email worker running` and stays in the foreground. Without it, verification and password reset emails are
enqueued but never delivered. Requests still succeed, which makes the symptom easy to misread.

Delivery also requires a valid `EMAIL_API_KEY`. With an empty key you can still exercise the queue, but Resend will
reject the send.

## Build and run the compiled output

```shell
npm run build   # tsc, output in build/
npm start       # node build/index.js
```

The worker's compiled entrypoint is `node build/workers/email-worker.js`. These are the two commands used in the
deployed environment.

## Tests

```shell
npm test              # Jest
npm run test:watch    # watch mode
npm run test:coverage # coverage report
```

Tests live in `__tests__` directories next to the code they cover. Most of them sit under `src/application`, one
per use case module (`courses`, `enrollment`, `gamification`, `registration`, `reviews`, `student-progress`,
`verification` and so on, plus `application/email/templates`), but they are not limited to that layer:

| Location                                  | Covers                                          |
| ----------------------------------------- | ----------------------------------------------- |
| `src/application/*/__tests__`           | Use cases, one directory per module.            |
| `src/infrastructure/security/__tests__` | Hashing and token primitives.                   |
| `src/infrastructure/storage/s3/__tests__` | The S3 client, including endpoint resolution and retry behaviour. |
| `src/interface/http/middlewares/__tests__` | HTTP middlewares such as `requireRole`.      |

HTTP level tests use `supertest`. When you touch code outside `src/application`, look for the sibling `__tests__`
directory there rather than assuming the coverage lives with the use cases.

## Linting

```shell
npm run lint
npm run lint:fix
```

## Troubleshooting

### The API starts and immediately exits

Symptom: `Unable to connect to the database`, then `Failed to initialize database`, then the process exits. If a
supervisor is restarting it, this looks like a crash loop.

Cause: `src/config/database.ts` chooses the connection string based on `NODE_ENV`:

```ts
const isProd = () => process.env.NODE_ENV === 'production'
const postgresUri = isProd() ? process.env.POSTGRES_URI : process.env.POSTGRES_URI_DEV
```

The value must be **exactly** `production` for `POSTGRES_URI` to be read. Anything else, including `staging`,
falls back to `POSTGRES_URI_DEV`. In a deployed environment that variable usually does not exist, so Sequelize gets an
empty connection string, `testDatabaseConnection()` throws, and `initializeDatabase()` calls `process.exit(1)`.

Fix: set `NODE_ENV=production` and provide `POSTGRES_URI` in deployed environments; set `NODE_ENV=development`
and provide `POSTGRES_URI_DEV` locally. Do not invent a third value.

Locally, also check that Compose is up and that the port in `POSTGRES_URI_DEV` is `5431`, not `5432`.

### Emails are never delivered / Redis errors

Symptoms: `NOAUTH Authentication required`, or jobs pile up in the queue and nothing is sent.

`src/infrastructure/queue/redis.ts` builds the connection from `REDIS_HOST`, `REDIS_PORT` and
`REDIS_PASSWORD`, and `REDIS_PASSWORD` has **no default**:

```ts
const redisPassword = process.env.REDIS_PASSWORD ?? undefined
```

- Local Compose Redis has **no** password, so leave `REDIS_PASSWORD` unset and point `REDIS_PORT` at `6380`.
- Any Redis instance that requires authentication (including the deployed one) needs `REDIS_PASSWORD` set, or every
  queue command is rejected.

Also confirm the worker process is actually running: the API alone only enqueues.

### `ECONNREFUSED` when uploading media

The S3 endpoint is wrong. Compose publishes MinIO on host port **9002**, not 9000. Check `S3_ENDPOINT` and that the
`educado-media` bucket exists (the `minio-setup` container creates it; re-run `docker compose up -d` if the
volume was wiped).

### `500 MISSING_ACCESS_TOKEN_SECRET` on authenticated routes

This error only happens with `NODE_ENV=production`. If you are seeing it locally, the real problem is that
`NODE_ENV` is set to `production` by mistake, not that the secret is missing.

`src/config/jwt.ts:13-21` resolves the signing secret in three steps:

```ts
const configuredSecret =
  process.env.ACCESS_TOKEN_SECRET ?? process.env.JWT_SECRET

if (configuredSecret && configuredSecret.trim() !== '') {
  return configuredSecret
}

if (process.env.NODE_ENV !== 'production') {
  // warns once, then:
  return 'dev-insecure-secret-change-me'
}

throw new AppError(500, { code: 'MISSING_ACCESS_TOKEN_SECRET' })
```

So:

- **Production** (`NODE_ENV=production`): a missing or blank secret throws `500 MISSING_ACCESS_TOKEN_SECRET` on
  every route that signs or verifies a token. Set `ACCESS_TOKEN_SECRET` (or its alias `JWT_SECRET`) and restart.
- **Anywhere else**, including local development: nothing is thrown. The API logs a single warning,
  `[auth] ACCESS_TOKEN_SECRET/JWT_SECRET não configurado; usando segredo temporário de desenvolvimento.`, and falls
  back to the hardcoded value `'dev-insecure-secret-change-me'`. Authentication keeps working.

!!! danger "The development fallback is easy to miss"

    The warning is emitted **once per process**, guarded by a module level flag, so it scrolls past on the very first
    authenticated request and never appears again. Nothing else signals the fallback.

    Consequences worth knowing:

    - Every developer running without the variable shares the same publicly known signing key, so a token minted on
      one machine is valid on any other one running in the same state.
    - The secret is in the repository. Any environment that is not exactly `NODE_ENV=production` and is reachable
      by someone else is effectively unauthenticated.
    - An environment intended to be production but misconfigured (`staging`, empty, unset) will not fail loudly here:
      it will quietly issue tokens signed with the hardcoded key. Note that `NODE_ENV` also drives the database
      selection, so that misconfiguration usually shows up as a crash loop first.

    Set `ACCESS_TOKEN_SECRET` in your local `.env` anyway. Generate one with `openssl rand -base64 48`.

### CORS errors from the web or mobile client

Outside production the API allows every origin, so a CORS error locally usually means `NODE_ENV` is set to
`production` by mistake. In production, add the client origin to the comma separated `FRONTEND_ORIGIN` list.

### Port already in use

Change `PORT` in `.env`, or find the offending process. The Compose host ports (5431, 6380, 9002, 9003) were chosen
to avoid the usual defaults, so a clash there normally means a previous Educado stack is still running:

```shell
docker compose down
```

Add `-v` to also drop the volumes and start from an empty database.
