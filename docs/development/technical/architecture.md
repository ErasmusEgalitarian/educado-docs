# System Architecture

[← Back to Main Page](../../index.md)

## Introduction

This document describes the architecture of the Educado platform as it is actually implemented today. It covers the
three applications (API, web, mobile), the data stores, the asynchronous email pipeline and the security model.

Related documents:

- [API Documentation](api.md) for the HTTP surface.
- [Database Schema](database-schema.md) for the relational model.
- [Deployment & Infrastructure](deployment.md) for the runtime topology and environment variables.
- [Tools & Dependencies](../tools.md) for the toolchain.

## System Overview

Educado is a gamified learning platform for waste pickers in Brazil. Students consume courses on the mobile app,
content creators build and manage courses on the web application, and administrators review creator registrations and
govern the catalog. Everything is served by a single REST API.

| Application | Repository      | Stack                                        | Audience            |
| ----------- | --------------- | -------------------------------------------- | ------------------- |
| API         | `educado-api` | Node.js 20, Express 5, TypeScript, Sequelize | All clients         |
| Web         | `educado-web` | Vite, TypeScript (no UI framework), nginx    | Creators and admins |
| Mobile      | `educado-app` | Expo SDK 56, React Native, Android first     | Students            |

Public environments:

| Environment | URL                                                                              |
| ----------- | -------------------------------------------------------------------------------- |
| API         | [https://api-educado.tominho.com](https://api-educado.tominho.com)               |
| Swagger UI  | [https://api-educado.tominho.com/docs/](https://api-educado.tominho.com/docs/)   |
| Web         | [https://educado.tominho.com](https://educado.tominho.com)                       |

### Technologies Used

| Concern                 | Technology                                                    |
| ----------------------- | ------------------------------------------------------------- |
| **Runtime**             | Node.js 20 (`engines.node >= 20`)                           |
| **HTTP framework**      | Express 5                                                     |
| **Language**            | TypeScript 5.9 across API, web and mobile                     |
| **Database**            | PostgreSQL 16 accessed through Sequelize 6                    |
| **Cache and queue**     | Redis 7.2 with BullMQ 5 (email queue)                         |
| **Object storage**      | MinIO, S3 compatible, driven by the AWS SDK v3 client         |
| **Transactional email** | Resend                                                        |
| **Authentication**      | JWT (`jsonwebtoken`), passwords hashed with bcryptjs        |
| **API docs**            | Swagger UI served by the API itself at `/docs/`             |
| **Web build**           | Vite 7, served in production by nginx                         |
| **Mobile**              | Expo SDK 56 with `expo-router`, React Native 0.85           |

!!! note

    The web application is plain TypeScript with a small hand written router (`src/app/router.ts`). There is no Vue,
    React or Angular in `educado-web`. React Native is used only in the mobile app.

## Component Architecture

```text
          educado-app (Expo / RN)        educado-web (Vite + nginx)
                     |                              |
                     +------- HTTPS / JWT ----------+
                                   |
                                   v
                     +-----------------------------+
                     |    educado-api (Express)    |
                     | routes -> application ->    |
                     | domain / infrastructure     |
                     +--+-----------+-----------+--+
                        |           |           |
              +---------v--+   +----v----+   +--v------------+
              | PostgreSQL |   | Redis 7 |   | MinIO (S3)    |
              | Sequelize  |   | BullMQ  |   | media assets  |
              +------------+   +----+----+   +---------------+
                                    |
                          +---------v---------+
                          | email worker      |
                          | Resend            |
                          +-------------------+
```

### API layering

The API source tree in `educado-api/src` is organised in layers rather than a flat MVC:

| Directory           | Responsibility                                                                                     |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| `routes/`         | Express routers, one directory per resource. Request parsing and HTTP status mapping only.          |
| `application/`    | Use cases (registration, catalog, enrollment, gamification, media, email, tags and so on).          |
| `domain/`         | Domain rules that do not depend on Express or Sequelize (registration, gamification).               |
| `infrastructure/` | Adapters: `queue/` (BullMQ and Redis), `storage/` (S3/MinIO), `email/` (Resend), `security/`. |
| `interface/http/` | Cross cutting middlewares: `auth-jwt`, `require-role`, `request-id`, `require-https`.         |
| `models/`         | Sequelize models and their associations (`models/index.ts`).                                      |
| `config/`         | `database.ts` (Sequelize bootstrap) and `jwt.ts` (token secret).                                 |
| `docs/`           | The OpenAPI 3.0.3 document served through Swagger UI.                                               |
| `workers/`        | Standalone process entrypoints, currently `email-worker.ts`.                                      |

### Processes

The backend runs as two independent Node processes built from the same codebase:

| Process | Command                                | Role                                                           |
| ------- | -------------------------------------- | -------------------------------------------------------------- |
| Web     | `node build/index.js`                | Serves the REST API and Swagger UI.                            |
| Worker  | `node build/workers/email-worker.js` | Consumes the BullMQ email queue and delivers through Resend.   |

### Domain model

Sequelize models live in `src/models` and are wired together in `src/models/index.ts`. The main aggregates:

| Aggregate    | Models                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------- |
| Identity     | `User`, `RegistrationProfile`, `RegistrationReview`, `EmailVerification`, `PasswordReset` |
| Catalog      | `Course`, `Section`, `Activity`, `Tag`, `CourseTag`, `Institution`                  |
| Learning     | `Enrollment`, `CourseProgress`, `SectionProgress`, `ActivityProgress`                 |
| Gamification | `PointsLedger`, `StudentStats`, `Badge`, `StudentBadge`                               |
| Recognition  | `Certificate`, `CourseReview`                                                             |
| Media        | `MediaAsset`                                                                                |

Key associations:

- A `Course` belongs to a `User` (the owner/creator) and has many `Section` records; each `Section` has many
  `Activity` records.
- `Course` and `Tag` form a many to many relation through `CourseTag`.
- Progress is a three level chain: `CourseProgress` has many `SectionProgress`, which has many
  `ActivityProgress`.
- A `User` has one `RegistrationProfile` and many `RegistrationReview` records, both as subject and as reviewer.
- A `User` has many `MediaAsset` records and points to one of them as the avatar (`avatarMediaId`).

Identifiers are UUIDs in PostgreSQL. Column level detail is in [Database Schema](database-schema.md).

Schema changes are applied by `sequelize.sync()` in `src/config/database.ts`. Outside production the sync runs with
`alter: true`; in production it never alters, so structural changes must be planned deliberately.

## Authentication and Authorization

- Login endpoints return a signed JWT. Clients send it as `Authorization: Bearer <token>`.
- `requireAuth` (`src/interface/http/middlewares/auth-jwt.ts`) verifies the token with `ACCESS_TOKEN_SECRET` and
  puts `{ userId, role }` into `res.locals.auth`.
- Roles are `ADMIN`, `STUDENT` and `USER` (the last one covers content creators). Route level enforcement uses
  `requireRole(...roles)`, which answers `403 FORBIDDEN` when the role is not allowed.
- Errors are returned as machine readable codes, for example `{ "code": "UNAUTHORIZED" }`.
- Creator accounts are not active on sign up: they create a registration that an administrator approves or rejects
  under `/admin/registrations`.
- Passwords are hashed with bcryptjs. Password reset is a three step flow (request, verify, reset) backed by the
  `PasswordReset` model.
- Media streaming (`/media/:id/stream`) accepts the token as a query parameter so that `<img>` and `<video>`
  tags can consume protected assets.

## Cross cutting concerns

| Concern       | Implementation                                                                                                                                 |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| CORS          | `FRONTEND_ORIGIN` holds a comma separated allowlist. Outside production every origin is allowed to speed up local work.                       |
| HTTPS         | `requireHttpsInProduction` rejects plain HTTP once `NODE_ENV=production`. `trust proxy` is on because the API sits behind a reverse proxy. |
| Request IDs   | `requestIdMiddleware` tags every request so logs can be correlated.                                                                          |
| Rate limiting | `express-rate-limit` on sensitive endpoints.                                                                                                 |
| Payload size  | `express.urlencoded` is capped; uploads go through `multer` straight to object storage.                                                    |

## Data Flow

### Media upload

1. The client authenticates and calls `POST /media/images` (or the multipart video init/part/complete flow).
2. The API streams the file to MinIO through the S3 client and records a `MediaAsset` row with the owner.
3. Reads go through `GET /media/images/:id`, `GET /media/videos/:id` or `GET /media/:id/stream`, which
   resolves the object from storage.

### Transactional email

1. A use case (email verification, password reset, registration decision) enqueues a job on the BullMQ queue backed by
   Redis.
2. The email worker process consumes the queue and delivers through Resend using `EMAIL_API_KEY` and `EMAIL_FROM`.
3. Failures stay in the queue and are retried by BullMQ, so a provider outage does not break the request path.

### Course consumption

1. The student browses `/catalog/courses` and enrolls through `/student/enrollments`.
2. Activity answers are posted to `/student/activities/:activityId/answer`, which updates the progress chain and
   writes to the points ledger.
3. On completion the platform issues a `Certificate`, downloadable as a PDF and verifiable through
   `/certificates/verify/:code`.

## Revision History

| Date       | Version | Changes                                                                                    | Authors       |
| ---------- | ------- | ------------------------------------------------------------------------------------------ | ------------- |
| 02/04/2024 | 0.1     | Document creation                                                                          |               |
| 06/04/2024 | 0.2     | Topics 1.1, 1.2, 1.3, and 3                                                                |               |
| 16/04/2024 | 0.3     | Documentation on Git Pages                                                                 |               |
| 09/09/2024 | 0.4     | Updated technologies and app type                                                          |               |
| 09/09/2024 | 0.5     | Technology adjustments                                                                     |               |
| 13/08/2026 | 1.0     | Full rewrite against the implemented system (PostgreSQL, Express 5, Vite web, Expo mobile) | Lucas Antunes |

[← Back to Main Page](../../index.md)
