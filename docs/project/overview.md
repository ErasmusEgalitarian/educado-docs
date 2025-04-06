# Project Overview

[← Back to Main Page](../index.md)

## Context


**Educado** is a web and mobile application developed as part of the **Egalitarian Erasmus Initiative**, an effort within the **Egalitarian SDG Challenge** and supported by the **Erasmus+ Programme**. The project involves collaboration among students from:

- **University of Brasília (Brazil)**  
- **Aalborg University (Denmark)**  
- **University of Minho (Portugal)**  
- **Saxion University (Netherlands)**  

Educado is designed to **empower waste pickers** by providing educational resources that improve their financial literacy, health, machine operation skills, and hygiene practices. Teachers can upload educational content through a web app, while waste pickers can access the classes through a mobile app. By equipping waste pickers with accessible learning tools, the project contributes to **Sustainable Development Goal (SDG) 4: Quality Education**.

---

### Objectives and Scope

#### Objectives:

* Develop a **web platform for teachers** to upload educational videos and materials.
* Develop a **mobile application** that delivers **educational content** tailored for waste pickers.
* Improve **financial literacy, health awareness, and professional skills** within the waste-picking community.
* Provide **easy-to-understand learning materials** through multimedia content.
* Promote **digital inclusion** by ensuring accessibility and usability of the application.

#### Scope:

**Included:**

- **Web platform** for teachers to upload videos and materials.
- **Mobile application** with **educational modules** on finance, health, machine operations, and hygiene.
* Machine learning models to detect performance anomalies and predict potential failures based on historical data.
* Alerting system with customizable thresholds and multi-channel notifications.
* Visual dashboard for displaying server health and performance metrics.

**Not Included:**

* Monitoring of non-server infrastructure components such as databases, network devices, or virtual machines (though these may be included in future iterations).
* Full end-to-end security monitoring (the focus is primarily on performance monitoring and anomaly detection).
* Monitoring for non-production environments (e.g., development and staging environments).

---

### Key Features and Deliverables

The key features and deliverables of this project include:

| Feature                            | Description                                                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Data Collection Service**  | Real-time ingestion of server performance metrics.                                                                     |
| **Anomaly Detection Engine** | Machine learning-based analysis for identifying anomalies and predicting failures.                                     |
| **Alerting System**          | Multi-channel notifications for administrators.                                                                        |
| **Web Dashboard**            | A user-friendly interface displaying real-time server status and health metrics.                                       |
| **Documentation and API**    | Comprehensive documentation on how to deploy, use, and integrate the monitoring platform with existing infrastructure. |

---

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
| 02/04/2024 | 0.1     | Document creation                 |         |
| 06/04/2024 | 0.2     | Updated Documentation, scope, key features and deliverables, timeline  still need changes   |     andreozzi    |

-

[← Back to Main Page](../index.md)
