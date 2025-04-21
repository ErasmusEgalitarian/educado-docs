# Product Backlog Building

[← Back to Main Page](../../index.md)

## Guide to Reviewing This Documentation

This document outlines the **functional and non-functional requirements** for the **Data Management System**, which integrates **a hardware-connected scale, an API, and a mobile application**. The documentation follows a structured approach to ensure clarity and completeness.

### **How to Use This Documentation**

- **Functional Requirements (FR-00)** - The key capabilities the system must implement.
- **Non-Functional Requirements (NFR-00)** - The quality attributes ensuring system performance, security, and usability.
- **Themes (TM-00)** - High-level system areas grouping functionalities.
- **Epics (EP-00)** - Major features that contribute to the system’s development.
- **Capabilities (C-00)** - The abilities the system must support.
- **Features (F-00)** - Specific technical functionalities fulfilling each capability.
- **User Stories (US-00)** - Individual use cases defining how users interact with the system.
- **Backlog** - A detailed, structured representation of all functionalities. (After have all topics, we can construct that)

Each section follows a progressive breakdown of the system’s structure, from high-level requirements to detailed functionalities.
Nothing in this document is set in stone; if you notice an error, please discuss it with the team
---

## **1. Functional Requirements**

> Defines the system's **core functionalities**.
> What the system must do

| FR-ID    | Description                                                          |
| ----- | -------------------------------------------------------------------- |
| FR-01 | The system must have an **User Authentication System**. |
| FR-02 | The system must have a **User Managment System**.        |
| FR-03 | The system must have a **Course Management System**.     |
| FR-04 | The system must have a **Midia Management System**.            |

---

## **2. Non-Functional Requirements**

> Specifies **quality attributes** that ensure the system meets expectations for **performance, security, usability, scalability, etc**...

| NFR-ID    | Description                                                                 | SQuaRE Characteristic                          |
| ------- | --------------------------------------------------------------------------- | ---------------------------------------------- |
| NFR-01  | The system must be accessible via modern browsers (compatible with Chrome, Firefox, Safari, and Edge). | Compatibility – Coexistence                   |
| NFR-02  | The system must ensure high availability, with at least 99% uptime.         | Reliability – Availability                     |
| NFR-03  | The system must guarantee data security, with encrypted authentication and protection against common attacks (e.g., SQL Injection, XSS). | Security – Protection Against Attacks         |
| NFR-04  | The system must have a response time of less than 2 seconds for 95% of requests. | Performance Efficiency – Response Time        |
| NFR-05  | The system must be horizontally scalable, allowing capacity increases as demand grows. | Performance Efficiency – Behavior Under Load  |
| NFR-06  | The system must be developed with clean, modular, and documented code.      | Maintainability – Analyzability               |
| NFR-07  | The system must comply with LGPD (General Data Protection Law).             | Compliance – Regulatory                        |
| NFR-08  | The system must support responsive navigation, adapting to different screen sizes (mobile, tablet, desktop). | Usability – Accessibility                     |
| NFR-09  | The system must provide adequate usability, following UX best practices (e.g., visual feedback, consistency, clear navigation). | Usability – Operability                       |
| NFR-10  | The system must allow data backup and restoration at defined intervals.     | Reliability – Recoverability                  |

---

## **3. Themes**

> **Themes** categorize **major system areas**, grouping functionalities under broad topics.

| FR-ID     | TH-ID  | Theme                               | Description                                                                 |
|--------|-------|-------------------------------------|-----------------------------------------------------------------------------|
| FR-01  | TH-01 | User Authentication and Session Management | Manage login, logout, and session persistence securely.                     |
| FR-01  | TH-02 | Access Control and Security Policies       | Define and enforce user permissions, roles, and access restrictions.        |
| FR-02  | TH-03 | User Profile and Role Management           | Handle user registration, profile editing, and role assignments.            |
| FR-02  | TH-04 | User Search and Account Control            | Enable filtering, listing, and controlling user account statuses.           |
| FR-03  | TH-05 | Course Creation and Content Management     | Allow creation and management of courses, modules, and educational content. |
| FR-03  | TH-06 | Course Enrollment and Progress Tracking    | Handle enrollment processes and monitor user progress in courses.           |
| FR-04  | TH-07 | Media Upload and Categorization            | Support uploading, organizing, and tagging various media types.             |
| FR-04  | TH-08 | Media Use and Integration in Courses       | Enable embedding and linking media within course content.                   |

---

## **4. Epics**

> **Epics** define **high-level features** that contribute to system development.

| FR-ID    | Theme-ID | Epic-ID | Epic                               | Description                                                                 |
|--------|------------|-----------|------------------------------------|-----------------------------------------------------------------------------|
| FR-01  | TH-01      | EP-01     | User Login and Registration        | Develop secure login, logout, and registration mechanisms.                  |
| FR-01  | TH-01      | EP-02     | Session Lifecycle Management       | Handle token issuance, refresh, and session expiration.                     |
| FR-01  | TH-02      | EP-03     | Password and Identity Recovery     | Implement recovery mechanisms like password reset and email confirmation.   |
| FR-01  | TH-02      | EP-04     | Multi-Factor Authentication (MFA) | Add additional layers of authentication for security.                       |
| FR-02  | TH-03      | EP-05     | User Profile CRUD                  | Allow full editing and visualization of user data.                          |
| FR-02  | TH-03      | EP-06     | Role Assignment System             | Define and assign roles such as Admin, Instructor, and Student.             |
| FR-02  | TH-04      | EP-07     | Account Status Management          | Enable account activation, deactivation, and suspension.                    |
| FR-02  | TH-04      | EP-08     | Advanced User Filtering            | Implement filtering by name, email, role, and status.                       |
| FR-03  | TH-05      | EP-09     | Course CRUD                        | Enable creation, update, and removal of course structures.                  |
| FR-03  | TH-05      | EP-10     | Lesson and Module Design           | Allow modular content within each course.                                   |
| FR-03  | TH-06      | EP-11     | Enrollment Control                 | Allow enrollment, cancellation, and waiting list handling.                  |
| FR-03  | TH-06      | EP-12     | Progress Tracking                  | Provide visual indicators of user course progress.                          |
| FR-04  | TH-07      | EP-13     | File Upload Engine                 | Enable media upload in various formats (images, audio, video, PDFs).        |
| FR-04  | TH-07      | EP-14     | Media Classification System        | Categorize media by type, topic, and course relevance.                      |
| FR-04  | TH-08      | EP-15     | Media Permissions and Access       | Define who can view, reuse, or download media content.                      |
| FR-04  | TH-08      | EP-16     | Media Embedding in Courses         | Enable reuse of uploaded media inside course content.                       |
| FR-01  | TH-02      | EP-17     | Access Logs and Audit Trail        | Track all user access and security-related events.                          |
| FR-03  | TH-06      | EP-18     | Certificate Issuance System        | Automatically generate certificates after course completion.                |
| FR-02  | TH-03      | EP-19     | Profile Picture and Personal Info  | Add support for profile pictures and extended metadata.                     |
| FR-04  | TH-08      | EP-20     | Media Preview and Playback         | Allow safe preview of media before downloading or embedding.                |

# Above here, we do have semantic context, just structure pattern

---

## **5. Capabilities**

> **Capabilities** describe the **system's technical abilities** to support key functionalities.

| #    | Capability                 | Description                                                       |
| ---- | -------------------------- | ----------------------------------------------------------------- |
| C-01 | Weight Measurement         | Accurately measure weight using the scale prototype.              |
| C-02 | Real-Time Data Processing  | Process weight data with minimal latency.                         |
| C-03 | Secure API Access          | Ensure authentication and authorization for API access.           |
| C-04 | Mobile User Interface      | Provide an intuitive mobile interface for waste pickers.          |
| C-05 | Multi-Center Support       | Allow multiple cooperative centers to use the system.             |
| C-06 | Environmental Resilience   | Ensure scale durability in dust, moisture, and impact conditions. |
| C-07 | Data Storage & Retrieval   | Store and retrieve weight data efficiently.                       |
| C-08 | Compliance with Guidelines | Follow best practices from the implementation guide.              |

(Additional capabilities …)

---

## **6. Features**

> **Features** define the **specific functionalities** required to implement each capability.

| #    | Feature                       | Description                                                       |
| ---- | ----------------------------- | ----------------------------------------------------------------- |
| F-01 | Scale Data Transmission       | Transmit weight data from the scale to the API.                   |
| F-02 | Mobile Weight Display         | Display real-time weight data on the mobile app.                  |
| F-03 | User Authentication           | Secure login system for API and app users.                        |
| F-04 | Offline Mode                  | Enable mobile app functionality without an internet connection.   |
| F-05 | Multi-Center Management       | Manage users and operations across multiple cooperative centers.  |
| F-06 | API Logging & Monitoring      | Track API requests and performance metrics.                       |
| F-07 | Data Export                   | Allow users to export collected data in CSV or JSON formats.      |
| F-08 | UI Accessibility Enhancements | Ensure the app is accessible for users with low digital literacy. |

(Additional features …)

---

## **7. User Stories**

> **User stories** describe **how different users interact with the system**, providing real-world scenarios.

| #     | Description                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| US-01 | As a scale operator, I want the equipment to perform precise measurements to avoid weighing errors.                                        |
| US-02 | As a scale operator, I want the equipment to have a digital display to view the weight before confirmation.                                |
| US-03 | As an administrator, I want the scale to be resistant to adverse environmental conditions (dust, moisture, impact) for greater durability. |
| US-04 | As a scale operator, I want the system to notify me if the scale is uncalibrated to ensure accuracy.                                       |
| US-05 | As an administrator, I want to configure different weighing modes in the system to meet operational needs.                                 |

(Additional user stories …)

---

## **8. Backlog**

O backlog do projeto é uma lista abrangente de todas as tarefas, funcionalidades e melhorias planejadas para o aplicativo. Ele serve como uma referência central para o que precisa ser desenvolvido, permitindo que a equipe de desenvolvimento tenha uma visão clara do escopo do projeto. Além disso, funciona como uma lista de funcionalidades que serão priorizadas e selecionadas para o escopo do MVP.

| Tema | Épico                                 | Capacidades                     | Features                                   | User Story | Descrição                                                                                                              |
| ---- | -------------------------------------- | ------------------------------- | ------------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F01 Registro de Médicos e Administradores | US01       | Como médico, eu gostaria de me registrar no sistema para ter credenciais de acesso                                      |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F05 Login de Médicos e Administradores    | US02       | Como médico, eu gostaria de realizar login no sistema para ter acesso ao conteúdo da plataforma                        |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F05 Login de Médicos e Administradores    | US03       | Como administrador, eu gostaria de realizar login no sistema para ter acesso às funcionalidades de gestão              |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F04 Edição de Perfil de Usuário         | US04       | Como usuário (médico ou administrador), eu gostaria de redefinir a minha senha para recuperar as credenciais de acesso |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F04 Edição de Perfil de Usuário         | US05       | Como usuário (médico ou administrador), eu gostaria de editar o meu perfil para atualizar as informações cadastradas |
| TM01 | EP02 Assinatura e Notificações       | C04 Gerenciamento de Finanças  | F12 Gerenciamento de Assinatura            | US06       | Como médico, eu gostaria de acessar área de finanças para gerenciar assinatura                                        |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F01 Registro de Médicos e Administradores | US07       | Como administrador, eu gostaria de criar outras contas administrador para auxiliar na gestão                            |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F02 Pesquisa e Listagem de Usuários       | US08       | Como administrador, eu gostaria de listar usuários para visualizar os usuários cadastrados                             |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F03 Edição e Exclusão de Usuários      | US09       | Como administrador, eu gostaria de editar um usuário para corrigir eventuais erros de cadastro                          |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F03 Edição e Exclusão de Usuários      | US10       | Como administrador, eu gostaria de excluir um usuário para retirar eventuais cadastros indevidos                        |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C01 Gerenciamento de Usuários  | F02 Pesquisa e Listagem de Usuários       | US11       | Como administrador, eu gostaria de pesquisar um usuário específico para encontrá-lo com mais facilidade               |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F06 Criação e Listagem de Documentos     | US12       | Como administrador, eu gostaria de criar um documento para adicionar novo material                                       |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F06 Criação e Listagem de Documentos     | US13       | Como administrador, eu gostaria de listar documentos para visualizar materiais cadastrados                               |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F07 Edição e Exclusão de Documentos     | US14       | Como administrador, eu gostaria de editar um documento para atualizar um material                                        |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F07 Edição e Exclusão de Documentos     | US15       | Como administrador, eu gostaria de excluir um documento para remover material defasado                                   |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F06 Criação e Listagem de Documentos     | US16       | Como administrador, eu gostaria de criar um assunto para complementar um documento já cadastrado                        |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F06 Criação e Listagem de Documentos     | US17       | Como administrador, eu gostaria de listar assuntos para visualizar os assuntos cadastrados em um documento               |
| TM01 | EP01 Gestão de Conteúdos e Usuários | C02 Gerenciamento de Conteúdos | F07 Edição e Exclusão de Documentos     | US18       | Como administrador, eu gostaria de editar um assunto para atualizar o material                                           |

## Revision History

| Date       | Version | Changes                           | Authors |
| ---------- | ------- | --------------------------------- | ------- |
| 02/04/2024 | 0.1     | Document creation                 |         |
| 06/04/2024 | 0.2     | Topics 1.1, 1.2, 1.3, and 3       |         |
| 16/04/2024 | 0.3     | Documentation on Git Pages        |         |
| 09/09/2024 | 0.4     | Updated technologies and app type |         |
| 09/09/2024 | 0.5     | Technology adjustments            |         |

[← Back to Main Page](../../index.md)
