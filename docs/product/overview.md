# Product Overview

[← Back to Main Page](../index.md)

**Educado** is a gamified learning platform designed to empower waste pickers through personal and educational growth.
The platform delivers simple and accessible courses, enriched with gamification elements (leaderboards, badges, progress tracking), and is co-created with universities to ensure quality and impact.

Educado is currently in active development by international teams and aims to provide an intuitive mobile-first experience for waste pickers, while content creators and administrators work primarily through the web platform.

---

## Core Features

| Feature Name              | Description                                                                                      | Benefit/Value                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **User Authentication**   | Simple student login via phone/SMS; creators and admins via email/password with role validation. | Low-barrier access for waste pickers, secure role-based permissions.         |
| **User Management**       | Profile editing for all users; admin approval for content creators.                              | Keeps user data accurate, ensures trusted creators, and supports governance. |
| **Course Management**     | Creators build and organize courses with lessons and modular blocks (text, video, images, PDF).  | Supports flexible, accessible, and diverse learning paths.                   |
| **Gamification System**   | Leaderboards, badges, and streaks linked to learning activities.                                 | Boosts motivation, engagement, and healthy competition.                      |
| **Certificates**          | Digital certificates auto-generated upon course completion.                                      | Provides recognition and proof of achievement for students.                  |
| **Reporting & Analytics** | Dashboards for admins to monitor course usage and student progress.                              | Enables data-driven improvements and accountability.                         |

---

## Target Audience

| Target Group         | Description                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **Waste Pickers**    | Main beneficiaries, gaining access to short, accessible training to support personal development. |
| **University Teams** | Professors and students from partner universities creating and curating educational content.      |
| **Admins**           | Governance and project managers ensuring compliance, quality, and strategic alignment.            |

---

## Benefits

| Benefit           | Description                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------- |
| **Accessibility** | Mobile-first design ensures ease of use for waste pickers with limited digital literacy. |
| **Engagement**    | Gamification encourages consistent participation and achievement recognition.            |
| **Scalability**   | Built to grow with more users, courses, and gamified activities.                         |
| **Collaboration** | Strengthens ties between universities, cooperatives, and international stakeholders.     |

---

## Technical Specifications

| Attribute             | Details                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Platform**          | Web for creators/admins; mobile app (Android first) for students.                                                                          |
| **Technology Stack**  | Mobile: Expo SDK 56 + React Native <br> Web: Vite + TypeScript, no UI framework, served by nginx <br> Backend: Node.js 20 + Express 5 + TypeScript |
| **Data Stores**       | PostgreSQL 16 (Sequelize), Redis 7.2 (BullMQ queue), MinIO for S3 compatible media storage.                                                |
| **Integrations**      | Resend for transactional email; JWT for authentication.                                                                                    |
| **Hosting**           | Containerised and deployed with Coolify 4.3.1 on the project's own VPS, behind Traefik. See [Deployment & Infrastructure](../development/technical/deployment.md). |
| **Public URLs**       | Web: [https://educado.tominho.com](https://educado.tominho.com) <br> API: [https://api-educado.tominho.com](https://api-educado.tominho.com) |
| **Supported Devices** | Android (priority), web browsers (desktop). iOS is not part of the current scope.                                                          |

---

## Product Roadmap

| Quarter | Milestones                                                                                          |
| ------- | --------------------------------------------------------------------------------------------------- |
| **Q1**  | MVP release: login, course creation, lessons with modular blocks, certificates, student progress.   |
| **Q2**  | Gamification features: leaderboards, badges, streaks; expanded content library.                     |
| **Q3**  | Advanced analytics, API integrations, and improved admin dashboards.                                |
| **Q4**  | Scalability features: compliance, governance logs, multilingual support, and expanded partnerships. |

---

[← Back to Main Page](../index.md)
