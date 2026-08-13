# API Documentation: Educado Platform

[← Back to Main Page](../../index.md)

This page is a map of the Educado REST API: base URLs, authentication, and the routers that are actually mounted by
the application.

!!! important "Swagger is the canonical source"

    The OpenAPI document lives in the API repository (`educado-api/src/docs/swagger.ts`) and is served by the API
    itself. Request and response schemas, field names and status codes are authoritative there, not here.

    - Deployed: [https://api-educado.tominho.com/docs/](https://api-educado.tominho.com/docs/)
    - Local: `http://localhost:5001/docs/`

    If this page and Swagger disagree, Swagger wins and this page is the bug.

## Base URL

| Environment | Base URL                                                           |
| ----------- | ------------------------------------------------------------------ |
| Production  | [https://api-educado.tominho.com](https://api-educado.tominho.com) |
| Local       | `http://localhost:5001` (see `PORT` in the API `.env`)         |

There is no `/api` prefix. Routers are mounted directly at the root, so a course listing is
`GET https://api-educado.tominho.com/courses`.

The web application reads the base URL from `VITE_API_URL` at build time and falls back to `http://localhost:5001`.

## Authentication

Protected requests carry a JWT in the `Authorization` header:

```http
Authorization: Bearer <your-jwt-token>
```

Tokens are issued by the login endpoints (`POST /auth/login`, `POST /user/login`, and the student login endpoints
under `/student/auth`). The token payload carries the subject (`sub`) and the `role`, which is one of `ADMIN`,
`STUDENT` or `USER` (content creator). Routes guard themselves with `requireAuth` and `requireRole`.

`GET /media/:id/stream` also accepts the token as a `token` query parameter so that `<img>` and `<video>` tags
can load protected assets.

Errors use machine readable codes, for example:

```json
{ "code": "UNAUTHORIZED" }
```

## Mounted routers

These are the routers mounted in `educado-api/src/index.ts`.

| Mount point                     | Purpose                                                                    |
| ------------------------------- | -------------------------------------------------------------------------- |
| `/user`                       | Legacy user login and identity lookup.                                     |
| `/auth`                       | Creator registration, login and password reset.                            |
| `/admin`                      | Administrative review of users, registrations and media.                   |
| `/me`                         | Everything scoped to the authenticated user (profile, avatar, media).      |
| `/courses`                    | Course CRUD and activation for creators and admins.                        |
| `/sections`                   | Sections inside a course.                                                  |
| `/activities`                 | Activities inside a section.                                               |
| `/progress`                   | Progress records per user and course.                                      |
| `/certificates`               | Certificate issuing, listing and public verification.                      |
| `/tags`                       | Course tags.                                                               |
| `/institutions`               | Partner institutions.                                                      |
| `/account/email-verification` | Send and confirm the email verification code.                              |
| `/media`                      | Image and video upload, metadata and streaming.                            |
| `/student`                    | The mobile app surface (auth, profile, enrollments, progress, gamification). |
| `/catalog`                    | Public course discovery.                                                   |
| `/leaderboard`                | Global and per course rankings.                                            |
| `/docs`                       | Swagger UI.                                                                |

## Endpoint reference

### Auth and users

| Endpoint                              | Method | Description                                     |
| ------------------------------------- | ------ | ----------------------------------------------- |
| `/auth/registrations`               | POST   | Submit a creator registration.                  |
| `/auth/registrations/me/profile`    | PUT    | Update the profile of your own registration.    |
| `/auth/registrations/:userId/profile` | PUT  | Update another registration profile (admin).    |
| `/auth/registrations/me/status`     | GET    | Check the status of your registration.          |
| `/auth/login`                       | POST   | Log in and receive a JWT.                       |
| `/auth/password-reset/request`      | POST   | Request a reset code.                           |
| `/auth/password-reset/verify`       | POST   | Verify the reset code.                          |
| `/auth/password-reset/reset`        | POST   | Set the new password.                           |
| `/user/login`                       | POST   | Legacy login.                                   |
| `/user/me`                          | POST   | Resolve the current user.                       |
| `/account/email-verification/send`    | POST   | Send an email verification code.                |
| `/account/email-verification/confirm` | POST   | Confirm the code.                               |

### Authenticated user (`/me`)

| Endpoint                     | Method | Description                          |
| ---------------------------- | ------ | ------------------------------------ |
| `/me/profile`              | GET    | Read your profile.                   |
| `/me/profile`              | PUT    | Update your profile.                 |
| `/me/avatar`               | PUT    | Set the avatar from a media asset.   |
| `/me/avatar`               | DELETE | Remove the avatar.                   |
| `/me/courses`              | GET    | Courses you own or are enrolled in.  |
| `/me/media`                | GET    | Media assets you own.                |
| `/me/password/request-code` | POST  | Request a password change code.      |
| `/me/account`              | DELETE | Delete your own account.             |

### Administration (`/admin`)

| Endpoint                                | Method | Description                              |
| --------------------------------------- | ------ | ---------------------------------------- |
| `/admin/users`                        | GET    | List users.                              |
| `/admin/users/:userId`                | GET    | User detail.                             |
| `/admin/users/:userId/role`           | PATCH  | Change a user role.                      |
| `/admin/users/:userId`                | DELETE | Remove a user.                           |
| `/admin/registrations`                | GET    | List pending registrations.              |
| `/admin/registrations/:userId/approve` | POST  | Approve a creator registration.          |
| `/admin/registrations/:userId/reject` | POST   | Reject a creator registration.           |
| `/admin/media`                        | GET    | List media across the platform.          |

### Content

| Endpoint                       | Method | Description                          |
| ------------------------------ | ------ | ------------------------------------ |
| `/courses`                   | GET    | List courses.                        |
| `/courses`                   | POST   | Create a course.                     |
| `/courses/:id`               | GET    | Course detail.                       |
| `/courses/:id`               | PUT    | Update a course.                     |
| `/courses/:id/activate`      | POST   | Publish a course.                    |
| `/courses/:id/deactivate`    | POST   | Unpublish a course.                  |
| `/courses/:id`               | DELETE | Delete a course.                     |
| `/sections`                  | GET    | List sections.                       |
| `/sections`                  | POST   | Create a section.                    |
| `/sections/:id`              | GET    | Section detail.                      |
| `/sections/:id`              | PUT    | Update a section.                    |
| `/sections/:id`              | DELETE | Delete a section.                    |
| `/activities/section/:sectionId` | GET | Activities of a section.            |
| `/activities/:id`            | GET    | Activity detail.                     |
| `/activities`                | POST   | Create an activity.                  |
| `/activities/:id`            | PUT    | Update an activity.                  |
| `/activities/:id`            | DELETE | Delete an activity.                  |
| `/tags`                      | GET    | List tags.                           |
| `/tags/:id`                  | GET    | Tag detail.                          |
| `/tags`                      | POST   | Create a tag.                        |
| `/tags/:id`                  | PUT    | Update a tag.                        |
| `/tags/:id`                  | DELETE | Delete a tag.                        |
| `/institutions`              | GET    | List institutions.                   |
| `/institutions/:id`          | GET    | Institution detail.                  |
| `/institutions`              | POST   | Create an institution.               |
| `/institutions/:id`          | PUT    | Update an institution.               |
| `/institutions/:id`          | DELETE | Delete an institution.               |

### Catalog and leaderboard

| Endpoint                          | Method | Description                         |
| --------------------------------- | ------ | ----------------------------------- |
| `/catalog/courses`              | GET    | Browse the published catalog.       |
| `/catalog/courses/:id`          | GET    | Public course detail.               |
| `/catalog/courses/:id/reviews`  | GET    | Reviews of a course.                |
| `/catalog/categories`           | GET    | Catalog categories.                 |
| `/leaderboard/global`           | GET    | Global ranking.                     |
| `/leaderboard/courses/:courseId` | GET   | Ranking within a course.            |

### Student surface (`/student`)

| Endpoint                                  | Method | Description                              |
| ----------------------------------------- | ------ | ---------------------------------------- |
| `/student/auth/register`                | POST   | Register a student.                      |
| `/student/auth/device-login`            | POST   | Log in with a device identifier.         |
| `/student/auth/phone-login`             | POST   | Log in with a phone number.              |
| `/student/auth/email-login`             | POST   | Log in with email and password.          |
| `/student/profile`                      | GET    | Student profile.                         |
| `/student/profile`                      | PUT    | Update the student profile.              |
| `/student/account`                      | DELETE | Delete the student account.              |
| `/student/enrollments`                  | POST   | Enroll in a course.                      |
| `/student/enrollments`                  | GET    | List enrollments.                        |
| `/student/enrollments/:courseId`        | GET    | Enrollment detail.                       |
| `/student/enrollments/:courseId`        | DELETE | Cancel an enrollment.                    |
| `/student/progress/courses`             | GET    | Progress across courses.                 |
| `/student/progress/courses/:courseId`   | GET    | Progress in one course.                  |
| `/student/progress/courses/:courseId/sections/:sectionId` | POST | Record progress on one section. |
| `/student/progress/courses/:courseId/complete` | PUT | Mark the course as complete for the authenticated student. |
| `/student/activities/:activityId/answer` | POST  | Submit an activity answer.               |
| `/student/gamification/summary`         | GET    | Points, streak and level summary.        |
| `/student/gamification/badges`          | GET    | Badges earned.                           |
| `/student/gamification/points-history`  | GET    | Points ledger.                           |
| `/student/reviews`                      | POST   | Review a course.                         |
| `/student/reviews/check/:courseId`      | GET    | Whether the course was already reviewed. |
| `/student/certificates`                 | GET    | Certificates earned.                     |
| `/student/certificates/:id/pdf`         | GET    | Download a certificate as PDF.           |

### Progress and certificates (creator/admin view)

| Endpoint                                                       | Method | Description                       |
| -------------------------------------------------------------- | ------ | --------------------------------- |
| `/progress/:username/courses`                                | GET    | Progress records of a user.       |
| `/progress/:username/courses/:courseId`                      | GET    | Progress in one course.           |
| `/progress/:username/courses/:courseId/sections/:sectionId`  | POST   | Record section progress.          |
| `/progress/:username/courses/:courseId/complete`             | PUT    | Mark a course as complete.        |
| `/certificates/:username`                                    | GET    | Certificates of a user.           |
| `/certificates`                                              | POST   | Issue a certificate.              |
| `/certificates/verify/:code`                                 | GET    | Public certificate verification.  |

### Media (`/media`)

| Endpoint                       | Method | Description                                   |
| ------------------------------ | ------ | --------------------------------------------- |
| `/media/images`              | POST   | Upload an image.                              |
| `/media/images/:id`          | GET    | Image metadata and access.                    |
| `/media/images/:id/metadata` | POST / PUT | Update image metadata.                    |
| `/media/images/:id`          | DELETE | Delete an image.                              |
| `/media/videos`              | POST   | Upload a video in a single request. Legacy, kept for backward compatibility. |
| `/media/videos/init`         | POST   | Start a multipart video upload.               |
| `/media/videos/:id/parts/:partNumber` | POST | Upload one part of a multipart upload. Field name `chunk`, `partNumber` starts at 1. |
| `/media/videos/:id/complete` | POST   | Complete a multipart upload.                  |
| `/media/videos/:id/abort`    | POST   | Abort a multipart upload.                     |
| `/media/videos/:id`          | GET    | Video metadata and access.                    |
| `/media/videos/:id/metadata` | POST / PUT | Update video metadata.                    |
| `/media/videos/:id`          | DELETE | Delete a video.                               |
| `/media/:id/stream`          | GET    | Stream an asset, token accepted in the query. |

!!! note "Video upload is a three call sequence"

    `POST /media/videos/init` only opens the multipart upload; it moves no bytes. The actual content is sent by
    `POST /media/videos/:id/parts/:partNumber`, once per chunk, as `multipart/form-data` with the file under the
    field name `chunk`. `POST /media/videos/:id/complete` then assembles the parts, and
    `POST /media/videos/:id/abort` discards them.

    Parts are capped at 60 MB server side, sized for a 50 MB client chunk plus framing overhead. Prefer this flow
    over the single request `POST /media/videos`, which is bounded by the 100 MB body limit imposed by Cloudflare in
    front of the API. See [Deployment & Infrastructure](deployment.md).

## Response Codes

- `200 OK`: request succeeded.
- `201 Created`: resource created successfully.
- `400 Bad Request`: invalid input.
- `401 Unauthorized`: authentication required or failed.
- `403 Forbidden`: insufficient permissions.
- `404 Not Found`: resource not found.
- `409 Conflict`: resource conflict (for example, duplicate email).
- `500 Internal Server Error`: unhandled error.

[← Back to Main Page](../../index.md)
