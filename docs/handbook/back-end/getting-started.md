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

Tests live in `__tests__` directories next to the use cases they cover, under `src/application`, and HTTP level
tests use `supertest`.

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

`ACCESS_TOKEN_SECRET` is missing or empty in `.env`. Set it and restart the API.

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
