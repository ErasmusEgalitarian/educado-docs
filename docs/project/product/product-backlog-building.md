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
| FR-01 | TH-01 | User Authentication System                 | Manage login, registration, and session security.                           |
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

## **4. Epics and Capabilities**

> Each Epic is broken down into at least two capabilities, representing sub-functionalities.

| EP-ID | Epic Name (from original document) | Capabilities (ID: Name)                                                                                                                               |
|-------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| EP-01 | User Login and Registration        | C-EP01-01: User Identity VerificationC-EP01-02: Account Creation Workflow                                                                        |
| EP-02 | Session Lifecycle Management       | C-EP02-01: Secure Session EstablishmentC-EP02-02: Session Duration Control                                                                         |
| EP-03 | Password and Identity Recovery     | C-EP03-01: Secure Password Reset MechanismsC-EP03-02: Identity Confirmation Methods                                                                 |
| EP-04 | Multi-Factor Authentication (MFA)  | C-EP04-01: MFA Method ConfigurationC-EP04-02: MFA Challenge-Response Handling                                                                      |
| EP-05 | User Profile CRUD                  | C-EP05-01: Profile Data ManagementC-EP05-02: Profile Information Presentation                                                                      |
| EP-06 | Role Assignment System             | C-EP06-01: Role Definition and ManagementC-EP06-02: User-Role Mapping                                                                              |
| EP-07 | Account Status Management          | C-EP07-01: Account Lifecycle ControlC-EP07-02: Status Change Auditing                                                                              |
| EP-08 | Advanced User Filtering            | C-EP08-01: Complex Query ConstructionC-EP08-02: Filterable User Attributes                                                                         |
| EP-09 | Course CRUD                        | C-EP09-01: Course Structure DefinitionC-EP09-02: Course Metadata Management                                                                        |
| EP-10 | Lesson and Module Design           | C-EP10-01: Content StructuringC-EP10-02: Learning Object Organization                                                                              |
| EP-11 | Enrollment Control                 | C-EP11-01: Enrollment Process ManagementC-EP11-02: Access Restriction Enforcement                                                                 |
| EP-12 | Progress Tracking                  | C-EP12-01: Learner Activity MonitoringC-EP12-02: Progress Data Visualization                                                                        |
| EP-13 | File Upload Engine                 | C-EP13-01: Media Ingestion and ProcessingC-EP13-02: File Storage Management                                                                        |
| EP-14 | Media Classification System        | C-EP14-01: Metadata TaggingC-EP14-02: Categorization Schemas                                                                                        |
| EP-15 | Media Permissions and Access       | C-EP15-01: Access Control Policy DefinitionC-EP15-02: Content Usage Rights Management                                                              |
| EP-16 | Media Embedding in Courses         | C-EP16-01: Media Integration ToolsC-EP16-02: Content Rendering and Display                                                                         |
| EP-17 | Access Logs and Audit Trail        | C-EP17-01: Event Logging MechanismC-EP17-02: Audit Log Review and Analysis                                                                          |
| EP-18 | Certificate Issuance System        | C-EP18-01: Completion Criteria VerificationC-EP18-02: Certificate Generation and Delivery                                                          |
| EP-19 | Profile Picture and Personal Info  | C-EP19-01: Personal Data CustomizationC-EP19-02: Profile Image Handling                                                                             |
| EP-20 | Media Preview and Playback         | C-EP20-01: Safe Content PreviewC-EP20-02: Multimedia Playback Controls                                                                              |
| EP-21 | Email Notification System          | C-EP21-01: Automated Email GenerationC-EP21-02: Email Delivery Management                                                                          |
| EP-22 | In-app Notification Center         | C-EP22-01: Notification AggregationC-EP22-02: Real-time Alert Display                                                                                |
| EP-23 | Course Analytics                   | C-EP23-01: Engagement Data CollectionC-EP23-02: Performance Metrics Reporting                                                                       |
| EP-24 | User Activity Reports              | C-EP24-01: System Usage TrackingC-EP24-02: Customizable Report Generation                                                                          |
| EP-25 | Course Assessment System           | C-EP25-01: Assessment Creation ToolsC-EP25-02: Grading and Feedback Mechanisms                                                                    |

---

## **5. Capabilities and Features**

> Each Capability is further refined into at least two Features, describing specific functionalities.

| Capability-ID | Capability Name                     | Features (ID: Name)                                                                                                                                    |
|---------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| C-EP01-01     | User Identity Verification          | FE-C01.1-01: Standard Credential AuthenticationFE-C01.1-02: Third-Party Identity Provider Integration                                               |
| C-EP01-02     | Account Creation Workflow           | FE-C01.2-01: User Registration FormFE-C01.2-02: Account Activation Process                                                                           |
| C-EP02-01     | Secure Session Establishment        | FE-C02.1-01: Encrypted Session Token GenerationFE-C02.1-02: Session Cookie Management                                                                 |
| C-EP02-02     | Session Duration Control            | FE-C02.2-01: Configurable Session TimeoutFE-C02.2-02: Session Renewal Mechanism                                                                       |
| C-EP03-01     | Secure Password Reset Mechanisms    | FE-C03.1-01: Email-Based Password Reset LinkFE-C03.1-02: Security Question Verification for Reset                                                      |
| C-EP03-02     | Identity Confirmation Methods       | FE-C03.2-01: Email Confirmation for Account ChangesFE-C03.2-02: SMS Code Verification                                                                  |
| C-EP04-01     | MFA Method Configuration            | FE-C04.1-01: Authenticator App Setup (TOTP)FE-C04.1-02: SMS/Email Code for MFA                                                                         |
| C-EP04-02     | MFA Challenge-Response Handling     | FE-C04.2-01: MFA Code Input and ValidationFE-C04.2-02: Backup Recovery Codes for MFA                                                                  |
| C-EP05-01     | Profile Data Management             | FE-C05.1-01: Editable User Profile FieldsFE-C05.1-02: Profile Data Validation and Sanitization                                                        |
| C-EP05-02     | Profile Information Presentation    | FE-C05.2-01: Public Profile ViewFE-C05.2-02: Private Profile Dashboard                                                                                |
| C-EP06-01     | Role Definition and Management      | FE-C06.1-01: Admin Interface for Role CreationFE-C06.1-02: Permission Assignment to Roles                                                              |
| C-EP06-02     | User-Role Mapping                   | FE-C06.2-01: Assigning Roles to UsersFE-C06.2-02: Viewing Users by Role                                                                                |
| C-EP07-01     | Account Lifecycle Control           | FE-C07.1-01: Account Activation/DeactivationFE-C07.1-02: Account Suspension/Deletion                                                                |
| C-EP07-02     | Status Change Auditing              | FE-C07.2-01: Logging of Account Status ChangesFE-C07.2-02: Notification of Status Changes                                                            |
| C-EP08-01     | Complex Query Construction          | FE-C08.1-01: Multi-Criteria User Search InterfaceFE-C08.1-02: Saved Search Filters                                                                    |
| C-EP08-02     | Filterable User Attributes          | FE-C08.2-01: Filtering by Profile Fields (Name, Email, etc.)FE-C08.2-02: Filtering by Account Status and Role                                        |
| C-EP09-01     | Course Structure Definition         | FE-C09.1-01: Course Creation WizardFE-C09.1-02: Course Outline Editor (Modules, Lessons)                                                              |
| C-EP09-02     | Course Metadata Management          | FE-C09.2-01: Editing Course Title, Description, CategoryFE-C09.2-02: Setting Course Difficulty and Duration                                           |
| C-EP10-01     | Content Structuring                 | FE-C10.1-01: Module and Lesson Creation ToolsFE-C10.1-02: Reordering of Course Content                                                                 |
| C-EP10-02     | Learning Object Organization        | FE-C10.2-01: Associating Media with LessonsFE-C10.2-02: Linking Quizzes and Assignments to Modules                                                    |
| C-EP11-01     | Enrollment Process Management       | FE-C11.1-01: Student Self-EnrollmentFE-C11.1-02: Instructor/Admin Manual Enrollment                                                                 |
| C-EP11-02     | Access Restriction Enforcement      | FE-C11.2-01: Prerequisite Checking for EnrollmentFE-C11.2-02: Enrollment Capacity Limits                                                              |
| C-EP12-01     | Learner Activity Monitoring         | FE-C12.1-01: Tracking Lesson Completion StatusFE-C12.1-02: Logging Time Spent on Activities                                                          |
| C-EP12-02     | Progress Data Visualization         | FE-C12.2-01: Student Progress DashboardFE-C12.2-02: Instructor View of Class Progress                                                                |
| C-EP13-01     | Media Ingestion and Processing      | FE-C13.1-01: Multi-Format File UploaderFE-C13.1-02: Background Media Transcoding                                                                     |
| C-EP13-02     | File Storage Management             | FE-C13.2-01: Integration with Cloud StorageFE-C13.2-02: Media Library Organization                                                                  |
| C-EP14-01     | Metadata Tagging                    | FE-C14.1-01: Manual Tagging InterfaceFE-C14.1-02: Suggested Tags Based on Content                                                                     |
| C-EP14-02     | Categorization Schemas              | FE-C14.2-01: Predefined Category ManagementFE-C14.2-02: Custom Category Creation                                                                      |
| C-EP15-01     | Access Control Policy Definition    | FE-C15.1-01: Setting Media Visibility (Public, Private, Course-Specific)FE-C15.1-02: Defining Download/Reuse Permissions                           |
| C-EP15-02     | Content Usage Rights Management     | FE-C15.2-01: Watermarking OptionsFE-C15.2-02: Licensing Information Display                                                                           |
| C-EP16-01     | Media Integration Tools             | FE-C16.1-01: Rich Text Editor with Media EmbeddingFE-C16.1-02: Media Picker from Library                                                              |
| C-EP16-02     | Content Rendering and Display       | FE-C16.2-01: Responsive Media PlayerFE-C16.2-02: Secure Media Streaming                                                                                |
| C-EP17-01     | Event Logging Mechanism             | FE-C17.1-01: Centralized Audit Log StorageFE-C17.1-02: Configurable Log Levels                                                                       |
| C-EP17-02     | Audit Log Review and Analysis       | FE-C17.2-01: Audit Log Search and Filtering InterfaceFE-C17.2-02: Export Audit Log Data                                                               |
| C-EP18-01     | Completion Criteria Verification    | FE-C18.1-01: Automated Check of Course RequirementsFE-C18.1-02: Manual Override for Completion                                                        |
| C-EP18-02     | Certificate Generation and Delivery | FE-C18.2-01: Customizable Certificate TemplatesFE-C18.2-02: PDF Certificate Download/Email                                                            |
| C-EP19-01     | Personal Data Customization         | FE-C19.1-01: Editing Extended Profile Information (Bio, Links)FE-C19.1-02: Privacy Settings for Profile Fields                                       |
| C-EP19-02     | Profile Image Handling              | FE-C19.2-01: Profile Picture Upload and CroppingFE-C19.2-02: Avatar Generation if No Picture                                                          |
| C-EP20-01     | Safe Content Preview                | FE-C20.1-01: Document Previewer (PDF, DOCX)FE-C20.1-02: Image Thumbnail Generation                                                                     |
| C-EP20-02     | Multimedia Playback Controls        | FE-C20.2-01: Video/Audio Player with Standard ControlsFE-C20.2-02: Subtitle/Caption Support                                                             |
| C-EP21-01     | Automated Email Generation          | FE-C21.1-01: Templated Email SystemFE-C21.1-02: Trigger-Based Email Dispatch (e.g., on registration, enrollment)                                   |
| C-EP21-02     | Email Delivery Management           | FE-C21.2-01: Email Queue and Sending ServiceFE-C21.2-02: Bounce and Complaint Handling                                                                 |
| C-EP22-01     | Notification Aggregation            | FE-C22.1-01: Central Notification Feed/PanelFE-C22.1-02: Grouping Similar Notifications                                                               |
| C-EP22-02     | Real-time Alert Display             | FE-C22.2-01: Unread Notification Badges/IndicatorsFE-C22.2-02: Desktop/Push Notification Options                                                      |
| C-EP23-01     | Engagement Data Collection          | FE-C23.1-01: Tracking Views, Clicks, CompletionsFE-C23.1-02: Quiz/Assignment Submission Tracking                                                      |
| C-EP23-02     | Performance Metrics Reporting       | FE-C23.2-01: Course Completion Rate ReportsFE-C23.2-02: Learner Performance Dashboards                                                               |
| C-EP24-01     | System Usage Tracking               | FE-C24.1-01: Login Frequency and Session Duration MonitoringFE-C24.1-02: Feature Usage Analytics                                                       |
| C-EP24-02     | Customizable Report Generation      | FE-C24.2-01: Report Builder with Selectable Metrics and FiltersFE-C24.2-02: Scheduled Report Delivery                                                |
| C-EP25-01     | Assessment Creation Tools           | FE-C25.1-01: Quiz Builder (Multiple Choice, True/False, etc.)FE-C25.1-02: Assignment Creation Interface (File Upload, Text Entry)                     |
| C-EP25-02     | Grading and Feedback Mechanisms     | FE-C25.2-01: Online Grading InterfaceFE-C25.2-02: Automated Scoring for Quizzes                                                                      |

---

## **6. Backlog**

| FR-ID | TH-ID | Theme                               | EP-ID | Epic                              | FE-ID | Feature                     | US-ID | User Story (máx 1 US por linha)                                                              | AC-ID | Acceptance Criteria                                                                              |
|-------|-------|-------------------------------------|-------|-----------------------------------|-------|-----------------------------|-------|----------------------------------------------------------------------------------------------|-------|--------------------------------------------------------------------------------------------------|
| FR-01 | TH-01 | User Authentication System          | EP-01 | User Authentication               | FE-01 | Login System                | US-01 | As a student, I want to authenticate my credentials to access my learning dashboard        | AC-01 | [ ] The system must validate email and password.                                                 |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-02 | [ ] The system must redirect to the student learning dashboard after successful login.           |
| FR-01 | TH-01 | User Authentication System          | EP-01 | User Authentication               | FE-01 | Login System                | US-02 | As a content creator, I want to authenticate my credentials to access the content management dashboard | AC-03 | [ ] The system must validate institutional email and password.                                   |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-04 | [ ] The system must redirect to the content management dashboard after successful login.       |
| FR-01 | TH-01 | User Authentication System          | EP-01 | User Authentication               | FE-01 | Login System                | US-03 | As an admin, I want to authenticate my credentials to access the administrative dashboard    | AC-05 | [ ] The system must validate admin credentials with enhanced security.                           |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-06 | [ ] The system must log all admin login attempts.                                                |
| FR-01 | TH-01 | User Authentication System          | EP-01 | User Authentication               | FE-02 | Multi-factor Authentication | US-04 | As a student, I want to enable 2FA to increase my account security                           | AC-07 | [ ] The system must provide email and SMS 2FA options.                                           |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-08 | [ ] The system must allow disabling 2FA if needed.                                               |
| FR-01 | TH-01 | User Authentication System          | EP-01 | User Authentication               | FE-02 | Multi-factor Authentication | US-05 | As an admin, I want to enforce 2FA for all admin accounts                                    | AC-09 | [ ] The system must require 2FA setup during admin account creation.                             |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-10 | [ ] The system must not allow bypassing 2FA for admin accounts.                                  |
| FR-01 | TH-01 | User Authentication System          | EP-02 | User Registration                 | FE-07 | Registration Form           | US-06 | As a visitor, I want to register as a student to get credentials                             | AC-11 | [ ] The system must collect name, email, student ID, and password.                               |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-12 | [ ] The system must validate the student ID format.                                              |
| FR-01 | TH-01 | User Authentication System          | EP-02 | User Registration                 | FE-07 | Registration Form           | US-07 | As a visitor, I want to register as a content creator to get credentials                     | AC-13 | [ ] The system must collect name, institutional email, department, and password.                 |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-14 | [ ] The system must validate the institutional email domain.                                     |
| FR-01 | TH-01 | User Authentication System          | EP-02 | User Registration                 | FE-07 | Registration Form           | US-08 | As an admin, I want to register a new admin to grant administrative access                   | AC-15 | [ ] The system must require current admin credentials to create new admin accounts.              |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-16 | [ ] The system must send notification to all existing admins about new admin creation.           |
| FR-01 | TH-01 | User Authentication System          | EP-02 | User Registration                 | FE-09 | Email Verification          | US-09 | As a visitor, I want to verify my email to complete my registration                          | AC-17 | [ ] The system must send a verification link to the provided email.                              |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-18 | [ ] The system must activate the account only after email verification.                          |
| FR-01 | TH-01 | User Authentication System          | EP-02 | User Registration                 | FE-09 | Email Verification          | US-10 | As a system administrator, I want users to verify their emails to ensure valid contact information | AC-19 | [ ] The system must limit account functionality until email verification is completed.           |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-20 | [ ] The system must provide a mechanism to resend verification emails.                           |
| FR-01 | TH-02 | Access Control and Security Policies| EP-03 | Password and Identity Recovery    | FE-13 | Password Reset              | US-11 | As a student, I want to reset my password when forgotten                                     | AC-21 | [ ] The system must verify student identity using student ID and email.                          |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-22 | [ ] The system must enforce password complexity requirements for new passwords.                  |
| FR-01 | TH-02 | Access Control and Security Policies| EP-03 | Password and Identity Recovery    | FE-13 | Password Reset              | US-12 | As a content creator, I want to reset my password when forgotten                             | AC-23 | [ ] The system must verify identity using institutional email and department.                    |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-24 | [ ] The system must notify department heads about password reset requests.                       |
| FR-02 | TH-03 | User Profile and Role Management    | EP-05 | User Profile Management           | FE-21 | Profile Editor              | US-13 | As a student, I want to update my profile information                                        | AC-25 | [ ] The system must allow editing name, contact info, and preferences.                           |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-26 | [ ] The system must prevent editing of official student ID.                                      |
| FR-02 | TH-03 | User Profile and Role Management    | EP-05 | User Profile Management           | FE-21 | Profile Editor              | US-14 | As a content creator, I want to update my profile and expertise areas                        | AC-27 | [ ] The system must allow editing name, contact info, and areas of expertise.                  |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-28 | [ ] The system must display expertise areas on public profile.                                   |
| FR-02 | TH-03 | User Profile and Role Management    | EP-05 | User Profile Management           | FE-23 | Profile Picture             | US-15 | As a student, I want to upload a profile picture to personalize my account                   | AC-29 | [ ] The system must support JPG and PNG formats up to 5MB.                                     |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-30 | [ ] The system must moderate uploaded images for appropriate content.                            |
| FR-02 | TH-03 | User Profile and Role Management    | EP-06 | Role Assignment System            | FE-25 | Role Management             | US-16 | As an admin, I want to assign different roles to users                                       | AC-31 | [ ] The system must provide interface to change user roles.                                      |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-32 | [ ] The system must log all role changes with admin ID who made changes.                         |
| FR-02 | TH-03 | User Profile and Role Management    | EP-06 | Role Assignment System            | FE-25 | Role Management             | US-17 | As a department head, I want to assign content creator roles to department members           | AC-33 | [ ] The system must restrict role assignment to department members only.                         |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-34 | [ ] The system must notify users when their role has changed.                                    |
| FR-03 | TH-05 | Course Creation and Content Management| EP-09 | Course Creation and Management  | FE-27 | Course Builder              | US-18 | As a content creator, I want to create a new course with basic settings                      | AC-35 | [ ] The system must collect course title, description, objectives, and prerequisites.          |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-36 | [ ] The system must assign the creator as course owner with full edit rights.                    |
| FR-03 | TH-05 | Course Creation and Content Management| EP-10 | Course Content Development      | FE-28 | Module Management           | US-19 | As a content creator, I want to organize course content into modules                         | AC-37 | [ ] The system must support creation of multiple course modules.                                 |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-38 | [ ] The system must allow reordering modules via drag-and-drop.                                |
| FR-03 | TH-06 | Course Enrollment and Progress Tracking| EP-11 | Enrollment Management        | FE-30 | Course Enrollment           | US-20 | As a student, I want to enroll in available courses                                          | AC-39 | [ ] The system must show available courses based on prerequisites.                             |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-40 | [ ] The system must confirm enrollment and add course to student dashboard.                      |
| FR-03 | TH-06 | Course Enrollment and Progress Tracking| EP-12 | Learning Progress Tracking   | FE-32 | Progress Dashboard          | US-21 | As a student, I want to view my progress in each course                                      | AC-41 | [ ] The system must display completion percentage for each enrolled course.                      |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-42 | [ ] The system must highlight next recommended actions for each course.                          |
| FR-04 | TH-07 | Media Upload and Categorization     | EP-13 | Media Upload System             | FE-34 | File Uploader               | US-22 | As a content creator, I want to upload various media files for my courses                    | AC-43 | [ ] The system must support video, audio, images, and documents.                               |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-44 | [ ] The system must show upload progress and confirm completion.                                 |
| FR-04 | TH-07 | Media Upload and Categorization     | EP-14 | Media Organization              | FE-36 | Media Tagging               | US-23 | As a content creator, I want to tag and categorize uploaded media                            | AC-45 | [ ] The system must provide predefined and custom tag options.                                   |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-46 | [ ] The system must allow filtering media by tags.                                               |
| FR-04 | TH-08 | Media Use and Integration in Courses| EP-15 | Media Access Control            | FE-38 | Media Permissions           | US-24 | As a content creator, I want to control who can access my uploaded media                     | AC-47 | [ ] The system must provide options for public, course-only, or private access levels.         |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-48 | [ ] The system must prevent unauthorized downloads of restricted media.                          |
| FR-04 | TH-08 | Media Use and Integration in Courses| EP-16 | Media Integration               | FE-40 | Media Embedding             | US-25 | As a content creator, I want to embed media into course content                              | AC-49 | [ ] The system must provide media browser with search and filter capabilities.                   |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-50 | [ ] The system must maintain proper formatting when media is embedded.                           |
| FR-05 | TH-09 | Notification Configuration and Delivery| EP-17 | Notification System        | FE-42 | Email Notifications         | US-26 | As a student, I want to receive email notifications about course updates                     | AC-51 | [ ] The system must send notifications for new content, deadlines, and announcements.          |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-52 | [ ] The system must use email templates with proper branding.                                    |
| FR-05 | TH-09 | Notification Configuration and Delivery| EP-18 | Notification Preferences   | FE-44 | Preference Settings         | US-27 | As a user, I want to configure which notifications I receive                                 | AC-53 | [ ] The system must provide granular control over notification types.                            |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-54 | [ ] The system must respect user preferences while enforcing critical notifications.             |
| FR-06 | TH-10 | Analytics Dashboard and Reporting   | EP-19 | Usage Analytics                 | FE-46 | Analytics Dashboard         | US-28 | As a content creator, I want to see engagement metrics for my courses                        | AC-55 | [ ] The system must display views, completion rates, and average time spent.                     |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-56 | [ ] The system must provide visual charts and graphs of key metrics.                             |
| FR-06 | TH-10 | Analytics Dashboard and Reporting   | EP-20 | Reporting System                | FE-48 | Report Generation           | US-29 | As an admin, I want to generate system usage reports                                         | AC-57 | [ ] The system must support generating reports by date range.                                    |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-58 | [ ] The system must allow exporting reports in PDF, Excel, and CSV formats.                      |
| FR-06 | TH-10 | Analytics Dashboard and Reporting   | EP-20 | Reporting System                | FE-49 | Data Visualization          | US-30 | As a department head, I want to visualize department course performance                        | AC-59 | [ ] The system must provide comparative analysis between different courses.                      |
|       |       |                                     |       |                                   |       |                             |       |                                                                                              | AC-60 | [ ] The system must identify trends over academic terms.                                         |

---

## Revision History

| Date       | Version | Changes                                                                                                  | Authors                                            |
|------------|---------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 2025-04-10 | 0.1     | Document creation                                                                                        | [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 2025-04-15 | 0.2     | PBB update content                                                                                       | [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 2025-05-13 | 1.0     | Completed all sections and added US                                                                      | [Pedro Rodrigues](https://github.com/pedro-prp)    |                   |

[← Back to Main Page](../../index.md)