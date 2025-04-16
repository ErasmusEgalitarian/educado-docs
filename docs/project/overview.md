# Project Overview

[← Back to Main Page](../index.md)

## Context


**Educado** is a web and mobile application developed as part of the **Egalitarian Erasmus Initiative**, an effort within the **Egalitarian SDG Challenge** and supported by the **Erasmus+ Programme**. The project involves collaboration among students from:

- **University of Brasília (Brazil)**  
- **Aalborg University (Denmark)**  
- **University of Minho (Portugal)**  
- **Saxion University (Netherlands)**  

Educado is designed to **empower waste pickers** by providing educational resources that improve their financial literacy and health. After approval, authorized users can upload Educational Content through the web app, while waste pickers can access the classes through a mobile app. By equipping waste pickers with accessible learning tools, the project contributes to **Sustainable Development Goal (SDG) 4: Quality Education**.

---

### Objectives and Scope

#### Objectives:

* Develop a **web platform** to upload educational videos and materials.
* Develop a **mobile application** that delivers **educational content** tailored for waste pickers.
* Improve **financial literacy, health awareness, and professional skills** within the waste-picking community.
* Provide **user-friendly learning materials** through multimedia content.
* Promote **digital inclusion** by ensuring accessibility and usability of the application.

#### Scope:

**Included:**

- **Web platform**: enables content creators to upload videos, documents, and educational materials.
- **Mobile application for waste pickers**: provides access to educational content, with an intuitive interface and offline mode support.
- **Tailored educational modules**: focused on financial literacy and health.
- **Data synchronization system**: ensures that content uploaded via the web is available in the mobile app.
- **Offline learning mode**: allows users to download modules and study without an internet connection.
- **User authentication and role management**: supports different user types (Content Creators and Waste Pickers) with appropriate permissions.
- **Accessibility and usability**: interfaces designed to accommodate users with low digital literacy or limited education.

**Not Included:**

- **Gamification systems** (e.g., points, badges, leaderboards).
- **Automated content translation** (multilingual support may be added in future versions).
- **Real-time learning analytics dashboards** (learning progress is stored locally and synced periodically).
- **Remote device management for mobile users**.

---

### Key Features and Deliverables

The key features and deliverables of this project include:


| **Feature**                            | **Description**                                                                                           |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Educational Content Upload**         | content creators can upload videos, PDFs, and other learning materials through the web platform.                 |
| **Mobile Learning App**                | Intuitive mobile application that allows waste pickers to view educational content in video format.      |
| **Categorized Learning Modules**       | Content is organized by topic: Finance and Health.                              |
| **Offline Access**                     | Enables content download for offline learning when internet is not available.                            |
| **User Authentication System**         | Role-based login and permissions for content creators and waste pickers.                                         |
| **Automatic Content Sync**             | Updates the mobile app with the latest materials uploaded by teachers.                                   |
| **Multi-device Support**               | Compatible with Android smartphones and emulators, with optional iOS support.                            |


### Technologies and Tools

| Technology Area        | Tools and Frameworks                                                                 |
|------------------------|---------------------------------------------------------------------------------------|
| **Frontend (Web)**     | Node.js, Express.js, React, Axios, Jest, Cypress for testing                         |
| **Frontend (Mobile)**  | Android (Kotlin), Firebase (authentication and storage)                              |
| **Backend**            | Node.js, Express.js, MongoDB with Mongoose, Docker, REST API                         |
| **Database**           | MongoDB (primary database via Mongoose), PostgreSQL (for structured data, if used)   |
| **Cloud Services**     | Google Cloud Platform (GCP) for backend infrastructure, Firebase, AWS (S3 for storage)|
| **Authentication & Security** | Google OAuth2, environment-based .env secrets, GCP service account JSON              |
| **Deployment**         | GitHub Actions (auto-deploy on staging branch), Docker Compose for container orchestration |
| **Testing**            | Jest (unit tests), Cypress (E2E tests for frontend)                                   |


---

### Timeline

The project is expected to be completed over the following phases:

| Phase             | Duration    | Tasks                                                                                                              |
| ----------------- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| **Phase 1** | 0-3 months  | Research, data collection infrastructure, initial prototype for anomaly detection.                                 |
| **Phase 2** | 3-6 months  | Development of the alerting system, integration with existing infrastructure, and machine learning model training. |
| **Phase 3** | 6-9 months  | Dashboard development, user interface design, and system optimizations.                                            |
| **Phase 4** | 9-12 months | Deployment, testing in real-world environments, and final adjustments based on user feedback.                      |

---

### Expected Impact


| Benefit                          | Description                                                               |
|----------------------------------|---------------------------------------------------------------------------|
| **Educational Empowerment**      | Enables waste pickers to acquire valuable financial and technical skills. |
| **Digital Inclusion**            | Provides access to learning materials through mobile and web technology.  |
| **Improved Work Efficiency**     | Educates users on best practices for waste handling and safety.          |
| **Scalability and Adaptability** | Can be expanded to other countries and adapted to different languages.  |

---


# Revision History

| Date       | Version | Changes                           | Authors |
| ---------- | ------- | --------------------------------- | ------- |
| 06/04/2024 | 0.1     | Updated Documentation, scope, key features and deliverables, timeline  still need changes   |     andreozzi    |
| 11/04/2024 | 0.2     | Scope and Key Features Updated.   | andreozzi |
| 16/04/2024 | 0.3     | Content creators upload videos to web plataform not only teachers.   | andreozzi |
-

[← Back to Main Page](../index.md)
