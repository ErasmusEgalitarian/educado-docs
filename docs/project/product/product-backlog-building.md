# Product Backlog Building

[← Back to Main Page](../../index.md)

## **1. Functional Requirements**

> Defines the system's **core functionalities**.
> What the system must do

| FR-ID | Description                                             |
|-------|---------------------------------------------------------|
| FR-01 | The system must have an **User Authentication System**. |
| FR-02 | The system must have a **User Managment System**.       |
| FR-03 | The system must have a **Course Management System**.    |
| FR-04 | The system must have a **Midia Management System**.     |

---

## **2. Non-Functional Requirements**

> Specifies **quality attributes** that ensure the system meets expectations for **performance, security, usability, scalability, etc**...

| NFR-ID | Description                                                                                                                              | SQuaRE Characteristic                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| NFR-01 | The system must be accessible via modern browsers (compatible with Chrome, Firefox, Safari, and Edge).                                   | Compatibility – Coexistence                  |
| NFR-02 | The system must ensure high availability, with at least 99% uptime.                                                                      | Reliability – Availability                   |
| NFR-03 | The system must guarantee data security, with encrypted authentication and protection against common attacks (e.g., SQL Injection, XSS). | Security – Protection Against Attacks        |
| NFR-04 | The system must have a response time of less than 2 seconds for 95% of requests.                                                         | Performance Efficiency – Response Time       |
| NFR-05 | The system must be horizontally scalable, allowing capacity increases as demand grows.                                                   | Performance Efficiency – Behavior Under Load |
| NFR-06 | The system must be developed with clean, modular, and documented code.                                                                   | Maintainability – Analyzability              |
| NFR-07 | The system must comply with LGPD (General Data Protection Law).                                                                          | Compliance – Regulatory                      |
| NFR-08 | The system must support responsive navigation, adapting to different screen sizes (mobile, tablet, desktop).                             | Usability – Accessibility                    |
| NFR-09 | The system must provide adequate usability, following UX best practices (e.g., visual feedback, consistency, clear navigation).          | Usability – Operability                      |
| NFR-10 | The system must allow data backup and restoration at defined intervals.                                                                  | Reliability – Recoverability                 |

---

## **3. Themes**

> **Themes** categorize **major system areas**, grouping functionalities under broad topics.

| FR-ID | TH-ID | Theme                                      | Description                                                                 |
|-------|-------|--------------------------------------------|-----------------------------------------------------------------------------|
| FR-01 | TH-01 | User Authentication and Session Management | Manage login, logout, and session persistence securely.                     |
| FR-01 | TH-02 | Access Control and Security Policies       | Define and enforce user permissions, roles, and access restrictions.        |
| FR-02 | TH-03 | User Profile and Role Management           | Handle user registration, profile editing, and role assignments.            |
| FR-02 | TH-04 | User Search and Account Control            | Enable filtering, listing, and controlling user account statuses.           |
| FR-03 | TH-05 | Course Creation and Content Management     | Allow creation and management of courses, modules, and educational content. |
| FR-03 | TH-06 | Course Enrollment and Progress Tracking    | Handle enrollment processes and monitor user progress in courses.           |
| FR-04 | TH-07 | Media Upload and Categorization            | Support uploading, organizing, and tagging various media types.             |
| FR-04 | TH-08 | Media Use and Integration in Courses       | Enable embedding and linking media within course content.                   |

---

## **4. Epics**

> **Epics** define **high-level features** that contribute to system development.

| FR-ID | Theme-ID | Epic-ID | Epic                              | Description                                                               |
|-------|----------|---------|-----------------------------------|---------------------------------------------------------------------------|
| FR-01 | TH-01    | EP-01   | User Login and Registration       | Develop secure login, logout, and registration mechanisms.                |
| FR-01 | TH-01    | EP-02   | Session Lifecycle Management      | Handle token issuance, refresh, and session expiration.                   |
| FR-01 | TH-02    | EP-03   | Password and Identity Recovery    | Implement recovery mechanisms like password reset and email confirmation. |
| FR-01 | TH-02    | EP-04   | Multi-Factor Authentication (MFA) | Add additional layers of authentication for security.                     |
| FR-02 | TH-03    | EP-05   | User Profile CRUD                 | Allow full editing and visualization of user data.                        |
| FR-02 | TH-03    | EP-06   | Role Assignment System            | Define and assign roles such as Admin, Instructor, and Student.           |
| FR-02 | TH-04    | EP-07   | Account Status Management         | Enable account activation, deactivation, and suspension.                  |
| FR-02 | TH-04    | EP-08   | Advanced User Filtering           | Implement filtering by name, email, role, and status.                     |
| FR-03 | TH-05    | EP-09   | Course CRUD                       | Enable creation, update, and removal of course structures.                |
| FR-03 | TH-05    | EP-10   | Lesson and Module Design          | Allow modular content within each course.                                 |
| FR-03 | TH-06    | EP-11   | Enrollment Control                | Allow enrollment, cancellation, and waiting list handling.                |
| FR-03 | TH-06    | EP-12   | Progress Tracking                 | Provide visual indicators of user course progress.                        |
| FR-04 | TH-07    | EP-13   | File Upload Engine                | Enable media upload in various formats (images, audio, video, PDFs).      |
| FR-04 | TH-07    | EP-14   | Media Classification System       | Categorize media by type, topic, and course relevance.                    |
| FR-04 | TH-08    | EP-15   | Media Permissions and Access      | Define who can view, reuse, or download media content.                    |
| FR-04 | TH-08    | EP-16   | Media Embedding in Courses        | Enable reuse of uploaded media inside course content.                     |
| FR-01 | TH-02    | EP-17   | Access Logs and Audit Trail       | Track all user access and security-related events.                        |
| FR-03 | TH-06    | EP-18   | Certificate Issuance System       | Automatically generate certificates after course completion.              |
| FR-02 | TH-03    | EP-19   | Profile Picture and Personal Info | Add support for profile pictures and extended metadata.                   |
| FR-04 | TH-08    | EP-20   | Media Preview and Playback        | Allow safe preview of media before downloading or embedding.              |

---

## **5. Capabilities**

> **Capabilities** describe the **system's technical abilities** to support key functionalities.

| #    | Capability | Description |
|------|------------|-------------|
| C-00 |            |             |

(Additional capabilities …)

---

## **6. Features**

> **Features** define the **specific functionalities** required to implement each capability.

| #    | Feature | Description |
|------|---------|-------------|
| F-00 |         |             |

(Additional features …)

---

## **7. User Stories**

> **User stories** describe **how different users interact with the system**, providing real-world scenarios.

| #     | Description |
|-------|-------------|
| US-00 |             |

(Additional user stories …)

---

## **8. Backlog**

| FR-ID | Theme-ID | Theme                                      | Epic-ID | Epic                              | Description                                                               |
|-------|----------|--------------------------------------------|---------|-----------------------------------|---------------------------------------------------------------------------|
| FR-01 | TH-01    | User Authentication and Session Management | EP-01   | User Login and Registration       | Develop secure login, logout, and registration mechanisms.                |
| FR-01 | TH-01    | User Authentication and Session Management | EP-02   | Session Lifecycle Management      | Handle token issuance, refresh, and session expiration.                   |
| FR-01 | TH-02    | Access Control and Security Policies       | EP-03   | Password and Identity Recovery    | Implement recovery mechanisms like password reset and email confirmation. |
| FR-01 | TH-02    | Access Control and Security Policies       | EP-04   | Multi-Factor Authentication (MFA) | Add additional layers of authentication for security.                     |
| FR-01 | TH-02    | Access Control and Security Policies       | EP-17   | Access Logs and Audit Trail       | Track all user access and security-related events.                        |
| FR-02 | TH-03    | User Profile and Role Management           | EP-05   | User Profile CRUD                 | Allow full editing and visualization of user data.                        |
| FR-02 | TH-03    | User Profile and Role Management           | EP-06   | Role Assignment System            | Define and assign roles such as Admin, Instructor, and Student.           |
| FR-02 | TH-03    | User Profile and Role Management           | EP-19   | Profile Picture and Personal Info | Add support for profile pictures and extended metadata.                   |
| FR-02 | TH-04    | User Search and Account Control            | EP-07   | Account Status Management         | Enable account activation, deactivation, and suspension.                  |
| FR-02 | TH-04    | User Search and Account Control            | EP-08   | Advanced User Filtering           | Implement filtering by name, email, role, and status.                     |
| FR-03 | TH-05    | Course Creation and Content Management     | EP-09   | Course CRUD                       | Enable creation, update, and removal of course structures.                |
| FR-03 | TH-05    | Course Creation and Content Management     | EP-10   | Lesson and Module Design          | Allow modular content within each course.                                 |
| FR-03 | TH-06    | Course Enrollment and Progress Tracking    | EP-11   | Enrollment Control                | Allow enrollment, cancellation, and waiting list handling.                |
| FR-03 | TH-06    | Course Enrollment and Progress Tracking    | EP-12   | Progress Tracking                 | Provide visual indicators of user course progress.                        |
| FR-03 | TH-06    | Course Enrollment and Progress Tracking    | EP-18   | Certificate Issuance System       | Automatically generate certificates after course completion.              |
| FR-04 | TH-07    | Media Upload and Categorization            | EP-13   | File Upload Engine                | Enable media upload in various formats (images, audio, video, PDFs).      |
| FR-04 | TH-07    | Media Upload and Categorization            | EP-14   | Media Classification System       | Categorize media by type, topic, and course relevance.                    |
| FR-04 | TH-08    | Media Use and Integration in Courses       | EP-15   | Media Permissions and Access      | Define who can view, reuse, or download media content.                    |
| FR-04 | TH-08    | Media Use and Integration in Courses       | EP-16   | Media Embedding in Courses        | Enable reuse of uploaded media inside course content.                     |
| FR-04 | TH-08    | Media Use and Integration in Courses       | EP-20   | Media Preview and Playback        | Allow safe preview of media before downloading or embedding.              |

## Revision History

| Date       | Version | Changes            | Authors                                            |
|------------|---------|--------------------|----------------------------------------------------|
| 2025-04-10 | 0.1     | Document creation  | [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 2025-04-15 | 0.2     | PBB update content | [Lucas Antunes](https://github.com/LucasGSAntunes) |

[← Back to Main Page](../../index.md)
