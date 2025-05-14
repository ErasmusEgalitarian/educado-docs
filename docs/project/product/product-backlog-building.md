# Product Backlog Building

[← Back to Main Page](../../index.md)

## **1. Functional Requirements**

> Defines the system's **core functionalities**.
> What the system must do

| FR-ID | Description                                             |
|-------|---------------------------------------------------------|
| FR-01 | The system must have an **User Authentication System**. |
| FR-02 | The system must have a **User Management System**.      |
| FR-03 | The system must have a **Course Management System**.    |
| FR-04 | The system must have a **Media Management System**.     |
| FR-05 | The system must have a **Notification System**.         |
| FR-06 | The system must have a **Reporting and Analytics System**. |

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
| NFR-11 | The system must support internationalization with multiple languages.                                                                    | Usability – Accessibility                    |
| NFR-12 | The system must maintain an audit trail of all critical operations.                                                                      | Security – Accountability                    |
| NFR-13 | The system must have automated testing coverage of at least 80% for critical components.                                                 | Maintainability – Testability                |

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
| FR-05 | TH-09 | Notification Configuration and Delivery    | Configure and send various types of notifications to users.                 |
| FR-06 | TH-10 | Analytics Dashboard and Reporting          | Generate insights and reports on system usage and course performance.       |

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
| FR-05 | TH-09    | EP-21   | Email Notification System         | Send email notifications for important system events.                     |
| FR-05 | TH-09    | EP-22   | In-app Notification Center        | Provide a centralized location for viewing all notifications.             |
| FR-06 | TH-10    | EP-23   | Course Analytics                  | Track and display metrics about course engagement and completion.         |
| FR-06 | TH-10    | EP-24   | User Activity Reports             | Generate reports on user activity and system usage.                       |
| FR-03 | TH-05    | EP-25   | Course Assessment System          | Create and manage quizzes, assignments, and other assessment tools.       |

---

## **5. Capabilities**

> **Capabilities** describe the **system's technical abilities** to support key functionalities.

| #    | Capability | Description |
|------|------------|-------------|
| C-01 | User Identity Management | Ability to create, verify, and manage user identities securely across the platform. |
| C-02 | Role-based Access Control | Ability to assign and enforce different permission levels based on user roles. |
| C-03 | Content Creation and Management | Ability to create, edit, organize, and publish educational content. |
| C-04 | Learning Path Management | Ability to define and track sequential learning experiences. |
| C-05 | Media Processing | Ability to handle, transform, and deliver various media formats. |
| C-06 | Progress Tracking | Ability to monitor and report on user advancement through courses. |
| C-07 | Notification Delivery | Ability to send timely alerts through multiple channels. |
| C-08 | Data Analytics | Ability to collect, process, and visualize usage and performance data. |
| C-09 | Security Enforcement | Ability to protect against unauthorized access and common security threats. |
| C-10 | System Integration | Ability to connect with external systems via APIs and other integration methods. |

---

## **6. Features**

> **Features** define the **specific functionalities** required to implement each capability.

| #    | Feature | Description |
|------|---------|-------------|
| F-01 | User Registration | Allow new users to create accounts with email verification. |
| F-02 | Login System | Authenticate users with username/email and password. |
| F-03 | Password Reset | Enable users to recover access through secure password reset. |
| F-04 | Two-Factor Authentication | Add an extra security layer using SMS, email, or authenticator apps. |
| F-05 | User Profile Management | Allow users to view and edit their personal information. |
| F-06 | Role Management | Assign and modify user roles (Admin, Instructor, Student). |
| F-07 | Account Status Control | Enable/disable user accounts and manage suspension periods. |
| F-08 | User Search | Find users by various criteria (name, email, status, role). |
| F-09 | Course Creation | Create new courses with title, description, and basic settings. |
| F-10 | Module Management | Organize course content into logical modules and sections. |
| F-11 | Course Enrollment | Allow students to join courses and instructors to manage enrollment. |
| F-12 | Progress Visualization | Show completion percentage and next steps for courses. |
| F-13 | Media Upload | Upload images, videos, documents, and audio files. |
| F-14 | Media Tagging | Categorize media with tags for better organization and search. |
| F-15 | Media Access Control | Set permissions for who can view or use specific media. |
| F-16 | Media Embedding | Insert media into course content with proper formatting. |
| F-17 | Security Logging | Record all security-related events for audit purposes. |
| F-18 | Certificate Generation | Create and issue digital certificates upon course completion. |
| F-19 | Profile Customization | Upload profile pictures and customize profile appearance. |
| F-20 | Media Preview | View media content before downloading or using it. |
| F-21 | Email Notifications | Send automated emails for important events and updates. |
| F-22 | Notification Center | Provide a central hub for viewing all system notifications. |
| F-23 | Course Analytics Dashboard | Display metrics on course engagement and completion. |
| F-24 | User Activity Reporting | Generate reports on user behavior and system usage. |
| F-25 | Quiz Creation | Build assessments with various question types. |
| F-26 | Assignment Submission | Allow file uploads and text submissions for assignments. |
| F-27 | Grading System | Record and display grades for course activities. |
| F-28 | Discussion Forums | Enable threaded discussions within courses. |
| F-29 | Calendar Integration | Sync course events with personal calendars. |
| F-30 | Mobile Responsiveness | Ensure proper display and functionality on mobile devices. |

---

## **7. User Stories**

> **User stories** describe **how different users interact with the system**, providing real-world scenarios.

| #     | Description |
|-------|-------------|
| US-01 | As a visitor, I want to register in the system to access available courses. |
| US-02 | As a user, I want to login with my email and password to access my account. |
| US-03 | As a user, I want to recover my password in case I forget it. |
| US-04 | As a user, I want to activate two-factor authentication to increase my account security. |
| US-05 | As a user, I want to edit my profile to keep my information updated. |
| US-06 | As an administrator, I want to assign different roles to users to control their permissions. |
| US-07 | As an administrator, I want to deactivate user accounts that violate the terms of use. |
| US-08 | As an administrator, I want to search for users by name, email, or role to manage their accounts. |
| US-09 | As an instructor, I want to create a new course with title, description, and basic settings. |
| US-10 | As an instructor, I want to organize course content into modules and lessons for a better learning experience. |
| US-11 | As a student, I want to enroll in courses to access their content. |
| US-12 | As a student, I want to view my progress in each course to know what I have already completed. |
| US-13 | As an instructor, I want to upload videos, images, and documents to enrich my courses. |
| US-14 | As an instructor, I want to categorize media with tags to facilitate organization and search. |
| US-15 | As an administrator, I want to define access permissions for different types of media. |
| US-16 | As an instructor, I want to embed media in course content with proper formatting. |
| US-17 | As an administrator, I want to record all security-related events for audit purposes. |
| US-18 | As a student, I want to receive a digital certificate after completing a course. |
| US-19 | As a user, I want to upload a profile picture to personalize my account. |
| US-20 | As a user, I want to preview media before downloading or using it. |
| US-21 | As a user, I want to receive email notifications about important updates. |
| US-22 | As a user, I want to access a notification center to view all my notifications. |
| US-23 | As an instructor, I want to view metrics about engagement and completion of my courses. |
| US-24 | As an administrator, I want to generate reports on user behavior and system usage. |
| US-25 | As an instructor, I want to create quizzes with different types of questions to evaluate students. |
| US-26 | As a student, I want to submit assignments through file uploads or text. |
| US-27 | As an instructor, I want to assign grades to student activities. |
| US-28 | As a student, I want to participate in discussion forums within courses. |
| US-29 | As a user, I want to sync course events with my personal calendar. |
| US-30 | As a user, I want to access the system through mobile devices with an appropriate experience. |
| US-31 | As an administrator, I want to monitor system performance to ensure its availability. |
| US-32 | As an instructor, I want to define prerequisites for my courses to ensure students have the necessary knowledge. |
| US-33 | As a student, I want to mark lessons as favorites to access them quickly later. |
| US-34 | As an instructor, I want to create time-limited assessments to test students' knowledge. |
| US-35 | As a student, I want to receive detailed feedback on my assessments. |
| US-36 | As an administrator, I want to configure backup policies to protect system data. |
| US-37 | As an instructor, I want to reuse content between different courses to save time. |
| US-38 | As a student, I want to filter courses by category, difficulty level, and rating. |
| US-39 | As a user, I want to change my notification preferences to control which alerts I receive. |
| US-40 | As an instructor, I want to export student performance data for external analysis. |

---

## **8. Backlog**

| FR-ID | Theme-ID | Theme                                      | Epic-ID | Epic                              | Description                                                               | Related US |
|-------|----------|--------------------------------------------|---------|-----------------------------------|---------------------------------------------------------------------------|------------|
| FR-01 | TH-01    | User Authentication and Session Management | EP-01   | User Login and Registration       | Develop secure login, logout, and registration mechanisms.                | US-01, US-02 |
| FR-01 | TH-01    | User Authentication and Session Management | EP-02   | Session Lifecycle Management      | Handle token issuance, refresh, and session expiration.                   | US-02 |
| FR-01 | TH-02    | Access Control and Security Policies       | EP-03   | Password and Identity Recovery    | Implement recovery mechanisms like password reset and email confirmation. | US-03 |
| FR-01 | TH-02    | Access Control and Security Policies       | EP-04   | Multi-Factor Authentication (MFA) | Add additional layers of authentication for security.                     | US-04 |
| FR-01 | TH-02    | Access Control and Security Policies       | EP-17   | Access Logs and Audit Trail       | Track all user access and security-related events.                        | US-17 |
| FR-02 | TH-03    | User Profile and Role Management           | EP-05   | User Profile CRUD                 | Allow full editing and visualization of user data.                        | US-05 |
| FR-02 | TH-03    | User Profile and Role Management           | EP-06   | Role Assignment System            | Define and assign roles such as Admin, Instructor, and Student.           | US-06 |
| FR-02 | TH-03    | User Profile and Role Management           | EP-19   | Profile Picture and Personal Info | Add support for profile pictures and extended metadata.                   | US-19 |
| FR-02 | TH-04    | User Search and Account Control            | EP-07   | Account Status Management         | Enable account activation, deactivation, and suspension.                  | US-07 |
| FR-02 | TH-04    | User Search and Account Control            | EP-08   | Advanced User Filtering           | Implement filtering by name, email, role, and status.                     | US-08 |
| FR-03 | TH-05    | Course Creation and Content Management     | EP-09   | Course CRUD                       | Enable creation, update, and removal of course structures.                | US-09 |
| FR-03 | TH-05    | Course Creation and Content Management     | EP-10   | Lesson and Module Design          | Allow modular content within each course.                                 | US-10 |
| FR-03 | TH-05    | Course Creation and Content Management     | EP-25   | Course Assessment System          | Create and manage quizzes, assignments, and other assessment tools.       | US-25, US-26, US-27, US-34, US-35 |
| FR-03 | TH-06    | Course Enrollment and Progress Tracking    | EP-11   | Enrollment Control                | Allow enrollment, cancellation, and waiting list handling.                | US-11, US-32, US-38 |
| FR-03 | TH-06    | Course Enrollment and Progress Tracking    | EP-12   | Progress Tracking                 | Provide visual indicators of user course progress.                        | US-12, US-33 |
| FR-03 | TH-06    | Course Enrollment and Progress Tracking    | EP-18   | Certificate Issuance System       | Automatically generate certificates after course completion.              | US-18 |
| FR-04 | TH-07    | Media Upload and Categorization            | EP-13   | File Upload Engine                | Enable media upload in various formats (images, audio, video, PDFs).      | US-13 |
| FR-04 | TH-07    | Media Upload and Categorization            | EP-14   | Media Classification System       | Categorize media by type, topic, and course relevance.                    | US-14 |
| FR-04 | TH-08    | Media Use and Integration in Courses       | EP-15   | Media Permissions and Access      | Define who can view, reuse, or download media content.                    | US-15 |
| FR-04 | TH-08    | Media Use and Integration in Courses       | EP-16   | Media Embedding in Courses        | Enable reuse of uploaded media inside course content.                     | US-16, US-37 |
| FR-04 | TH-08    | Media Use and Integration in Courses       | EP-20   | Media Preview and Playback        | Allow safe preview of media before downloading or embedding.              | US-20 |
| FR-05 | TH-09    | Notification Configuration and Delivery    | EP-21   | Email Notification System         | Send email notifications for important system events.                     | US-21, US-39 |
| FR-05 | TH-09    | Notification Configuration and Delivery    | EP-22   | In-app Notification Center        | Provide a centralized location for viewing all notifications.             | US-22, US-39 |
| FR-06 | TH-10    | Analytics Dashboard and Reporting          | EP-23   | Course Analytics                  | Track and display metrics about course engagement and completion.         | US-23, US-40 |
| FR-06 | TH-10    | Analytics Dashboard and Reporting          | EP-24   | User Activity Reports             | Generate reports on user activity and system usage.                       | US-24, US-31, US-36 |

---

## Revision History

| Date       | Version | Changes                                  | Authors                                            |
|------------|---------|------------------------------------------|----------------------------------------------------|
| 2025-04-10 | 0.1     | Document creation                        | [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 2025-04-15 | 0.2     | PBB update content                       | [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 2025-05-13 | 1.0     | Completed all sections and added US      | [Pedro Rodrigues](https://github.com/pedro-prp)    |

[← Back to Main Page](../../index.md)