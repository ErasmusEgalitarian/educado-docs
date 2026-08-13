
# Tools & Externals

[← Back to Main Page](../index.md)

The tools below are the ones actually used by the Educado project. For the runtime topology see
[Deployment & Infrastructure](technical/deployment.md), and for the system design see
[System Architecture](technical/architecture.md).

## Development and collaboration

| Tool                     | Description                                                                                  | Link                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **GitHub**               | Source hosting, code review and issue tracking for every Educado repository.                 | [GitHub](https://github.com/)                                    |
| **GitHub Actions**       | CI for the repositories, including the documentation build (`mkdocs build --strict`).      | [GitHub Actions](https://github.com/features/actions)            |
| **MkDocs Material**      | Static site generator behind this documentation.                                             | [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)  |
| **uv**                   | Python dependency manager used to run and build the documentation site.                      | [uv](https://docs.astral.sh/uv/)                                 |

## Back end

| Tool                | Description                                                                                        | Link                                                       |
| ------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Node.js 20**      | Runtime for the API and the email worker.                                                          | [Node.js](https://nodejs.org/)                             |
| **Express 5**       | HTTP framework used to build the REST API.                                                         | [Express](https://expressjs.com/)                          |
| **TypeScript**      | Language used across API, web and mobile.                                                          | [TypeScript](https://www.typescriptlang.org/)              |
| **Sequelize**       | ORM mapping the PostgreSQL schema to the models in `src/models`.                                 | [Sequelize](https://sequelize.org/)                        |
| **PostgreSQL 16**   | Relational database, single source of truth for platform data.                                     | [PostgreSQL](https://www.postgresql.org/)                  |
| **Redis 7.2**       | Backing store for the BullMQ job queue.                                                            | [Redis](https://redis.io/)                                 |
| **BullMQ**          | Job queue used for asynchronous email delivery.                                                    | [BullMQ](https://docs.bullmq.io/)                          |
| **MinIO**           | S3 compatible object storage for images and videos.                                                | [MinIO](https://min.io/)                                   |
| **Resend**          | Transactional email provider (verification, password reset, registration decisions).               | [Resend](https://resend.com/)                              |
| **Swagger UI**      | API documentation served by the API itself at `/docs/`.                                          | [Swagger](https://swagger.io/)                             |
| **Jest**            | Unit and integration test runner for the API, with `supertest` for HTTP level tests.             | [Jest](https://jestjs.io/)                                 |
| **ESLint + Prettier** | Linting and formatting for the TypeScript codebases.                                             | [ESLint](https://eslint.org/)                              |

## Front end

| Tool          | Description                                                                                       | Link                                             |
| ------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Vite**      | Build tool and dev server for the web application. The web app is plain TypeScript, no framework. | [Vite](https://vite.dev/)                        |
| **axios**     | HTTP client used by the web application.                                                          | [axios](https://axios-http.com/)                 |
| **nginx**     | Serves the built web assets in production and handles the SPA fallback.                           | [nginx](https://nginx.org/)                      |
| **Expo (SDK 56)** | Toolchain for the React Native mobile app, Android first.                                     | [Expo](https://expo.dev/)                        |
| **React Native** | UI framework for the mobile app.                                                               | [React Native](https://reactnative.dev/)         |
| **EAS Build** | Builds the mobile binaries (.apk / .aab) for distribution.                                        | [EAS Build](https://docs.expo.dev/build/introduction/) |

## Infrastructure and delivery

| Tool         | Description                                                                                                  | Link                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| **Coolify**  | Self hosted PaaS (version 4.3.1) that deploys and supervises the API, the email worker and the web app.       | [Coolify](https://coolify.io/)             |
| **Nixpacks** | Build strategy used by Coolify for the Node processes (API and email worker).                                | [Nixpacks](https://nixpacks.com/)          |
| **Docker**   | Containerisation. The web app ships a multi stage Dockerfile; local infrastructure runs via Docker Compose.   | [Docker](https://www.docker.com/)          |
| **Traefik**  | Reverse proxy managed by Coolify, terminating TLS for the public domains.                                    | [Traefik](https://traefik.io/)             |

## Testing and inspection

| Tool         | Description                                                       | Link                                        |
| ------------ | ----------------------------------------------------------------- | ------------------------------------------- |
| **Postman**  | Manual API exploration alongside Swagger UI.                      | [Postman](https://www.postman.com/)         |
| **Swagger UI** | Interactive contract for the API, canonical for request shapes. | [Swagger](https://swagger.io/)              |

---

[← Back to Main Page](../index.md)
