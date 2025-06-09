# API Documentation: Educado Platform

[← Back to Main Page](../../../index.md)

This documentation provides a comprehensive overview of the API for managing users, courses, content, enrollment, media, notifications, and progress within the Educado platform.

---

## Base URL

The base URL for all API requests is:


[https://api.educado.com](https://api.educado.com)


---

## Authentication

All requests requiring authentication must include a **Bearer token** in the `Authorization` header. The token is obtained after a successful login.

**Example:**

Authorization: Bearer <your-jwt-token>
---

## Endpoints

### 1. **User Management**

| Endpoint          | Method   | Description                             |
| ----------------- | -------- | --------------------------------------- |
| `/api/register`   | `POST`   | Registers a new user (student/creator). |
| `/api/login`      | `POST`   | Logs in a user and returns a JWT token. |
| `/api/users`      | `GET`    | Lists all users (Admin only).           |
| `/api/users/{id}` | `GET`    | Retrieves details of a user.            |
| `/api/users/{id}` | `PUT`    | Edits a user profile.                   |
| `/api/users/{id}` | `DELETE` | Deactivates a user (soft delete).       |

#### 1.1 User Registration

* **URL:** `/api/register`
* **Method:** `POST`
* **Request Body:**

  ```json
  {
    "name": "Alice",
    "email": "alice@example.com",
    "password": "Password123",
    "role": "student" or "creator"
  }
  ```
* **Responses:**

  * **201 Created**
  * **400 Bad Request**

#### 1.2 User Login

* **URL:** `/api/login`
* **Method:** `POST`
* **Request Body:**

  ```json
  {
    "email": "alice@example.com",
    "password": "Password123"
  }
  ```
* **Responses:**

  * **200 OK**: `{ "token": "<jwt-token>" }`
  * **401 Unauthorized**

#### 1.3 Get User List (Admin only)

* **URL:** `/api/users`
* **Method:** `GET`
* **Response:** `[{ "_id": "...", "name": "...", "email": "...", "role": "student" }]`

#### 1.4 Get User Details

* **URL:** `/api/users/{id}`
* **Method:** `GET`
* **Response:** `{ "_id": "...", "name": "...", "email": "...", "role": "...", ... }`

#### 1.5 Edit User Profile

* **URL:** `/api/users/{id}`
* **Method:** `PUT`
* **Request Body:**

  ```json
  {
    "name": "Alice Updated",
    "email": "alice.updated@example.com"
  }
  ```
* **Response:** `{ "message": "User updated successfully", "user": { ... } }`

#### 1.6 Deactivate User

* **URL:** `/api/users/{id}`
* **Method:** `DELETE`
* **Response:** `{ "message": "User deactivated successfully" }`

---

### 2. **Course Management**

| Endpoint            | Method   | Description                           |
| ------------------- | -------- | ------------------------------------- |
| `/api/courses`      | `POST`   | Creates a new course (creator/admin). |
| `/api/courses`      | `GET`    | Lists all courses.                    |
| `/api/courses/{id}` | `GET`    | Gets course details.                  |
| `/api/courses/{id}` | `PUT`    | Updates a course.                     |
| `/api/courses/{id}` | `DELETE` | Deactivates a course (soft delete).   |

#### 2.1 Create Course

* **URL:** `/api/courses`
* **Method:** `POST`
* **Request Body:**

  ```json
  {
    "title": "Waste Sorting Basics",
    "description": "Learn how to separate waste.",
    "creator_id": "uuid-of-creator"
  }
  ```
* **Response:** `{ "message": "Course created successfully", "course": { ... } }`

#### 2.2 List Courses

* **URL:** `/api/courses`
* **Method:** `GET`
* **Response:** `[ { "_id": "...", "title": "...", ... } ]`

#### 2.3 Course Details

* **URL:** `/api/courses/{id}`
* **Method:** `GET`
* **Response:** `{ "_id": "...", "title": "...", ... }`

#### 2.4 Update Course

* **URL:** `/api/courses/{id}`
* **Method:** `PUT`
* **Request Body:**

  ```json
  {
    "title": "Updated Course Title",
    "description": "New description."
  }
  ```
* **Response:** `{ "message": "Course updated successfully", "course": { ... } }`

#### 2.5 Deactivate Course

* **URL:** `/api/courses/{id}`
* **Method:** `DELETE`
* **Response:** `{ "message": "Course deactivated successfully" }`

---

### 3. **Module, Lesson, and Exercise Management**

| Endpoint                            | Method   | Description                      |
| ----------------------------------- | -------- | -------------------------------- |
| `/api/courses/{courseId}/modules`   | `POST`   | Creates a module in a course.    |
| `/api/modules/{id}`                 | `PUT`    | Updates a module.                |
| `/api/modules/{id}`                 | `DELETE` | Deactivates a module.            |
| `/api/modules/{moduleId}/lessons`   | `POST`   | Creates a lesson in a module.    |
| `/api/lessons/{id}`                 | `PUT`    | Updates a lesson.                |
| `/api/lessons/{id}`                 | `DELETE` | Deactivates a lesson.            |
| `/api/lessons/{lessonId}/exercises` | `POST`   | Creates an exercise in a lesson. |
| `/api/exercises/{id}`               | `PUT`    | Updates an exercise.             |
| `/api/exercises/{id}`               | `DELETE` | Deactivates an exercise.         |

---

### 4. **Enrollment**

| Endpoint                         | Method   | Description                                 |
| -------------------------------- | -------- | ------------------------------------------- |
| `/api/courses/{courseId}/enroll` | `POST`   | Enrolls the authenticated user in a course. |
| `/api/enrollments`               | `GET`    | Lists enrollments for authenticated user.   |
| `/api/enrollments/{id}`          | `DELETE` | Cancels an enrollment (soft delete).        |

---

### 5. **Progress Tracking**

| Endpoint        | Method | Description                                        |
| --------------- | ------ | -------------------------------------------------- |
| `/api/progress` | `GET`  | Lists progress records for the authenticated user. |
| `/api/progress` | `POST` | Updates or creates a progress record.              |

---

### 6. **Media Management**

| Endpoint                  | Method   | Description                          |
| ------------------------- | -------- | ------------------------------------ |
| `/api/media`              | `POST`   | Uploads media (image, video, audio). |
| `/api/media`              | `GET`    | Lists all media for the user.        |
| `/api/media/{id}`         | `GET`    | Gets media details.                  |
| `/api/media/{id}`         | `PUT`    | Updates media metadata.              |
| `/api/media/{id}`         | `DELETE` | Deletes (deactivates) media.         |
| `/api/courses/{id}/media` | `POST`   | Associates media to a course.        |
| `/api/courses/{id}/media` | `DELETE` | Removes media from a course.         |

---

### 7. **Notifications**

| Endpoint                  | Method   | Description                       |
| ------------------------- | -------- | --------------------------------- |
| `/api/notifications`      | `POST`   | Creates a notification.           |
| `/api/notifications`      | `GET`    | Lists notifications for the user. |
| `/api/notifications/{id}` | `PUT`    | Updates a notification.           |
| `/api/notifications/{id}` | `DELETE` | Deletes a notification.           |

---

## Response Codes

* `200 OK` – Request succeeded.
* `201 Created` – Resource created successfully.
* `400 Bad Request` – Invalid input.
* `401 Unauthorized` – Authentication required or failed.
* `403 Forbidden` – Insufficient permissions.
* `404 Not Found` – Resource not found.
* `409 Conflict` – Resource conflict (e.g., duplicate email).
* `500 Internal Server Error` – Unhandled error.

---

For further details on request/response formats, refer to the **OpenAPI/Swagger** specification.

[← Back to Main Page](../../../index.md)
