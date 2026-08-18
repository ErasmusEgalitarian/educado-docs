# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.8.5] - 2026-08-18

### Changed

- Bump `black` from 25.9.0 to 26.3.1 (dependency update)

## [2.8.4] - 2026-08-18

### Changed

- Bump `idna` from 3.10 to 3.15 (dependency update)

## [2.8.3] - 2026-08-18

### Changed

- Bump `urllib3` from 2.5.0 to 2.7.0 (dependency update)

## [2.8.2] - 2026-08-18

### Changed

- Bump `pymdown-extensions` from 10.16.1 to 11.0.1 (dependency update)

## [2.8.1] - 2026-08-18

### Changed

- Bump `requests` from 2.32.5 to 2.33.0 (dependency update)

## [2.8.0] - 2026-08-18

### Added

- `CODE_OF_CONDUCT.md`, previously missing from the repository
- `SECURITY.md`, previously missing from the repository, documenting how to report vulnerabilities

### Changed

- Project license switched from GPL-3.0 to Apache-2.0, to be consistent with the other three Educado
  repositories (`api`, `web`, `app`)
- README License section corrected: it now points to the actual `LICENSE` file and names Apache License 2.0
  instead of the stale GPL-3.0 reference

## [2.7.0] - 2026-08-13

### Added

- Deployment & Infrastructure page documenting the Cloudflare Tunnel and Coolify topology, domains, build
  strategies, the environment variables read by the API, and the operational traps around `NODE_ENV`,
  `S3_ENDPOINTS`, `CERTIFICATE_VERIFICATION_URL` and the Cloudflare 100 MB request body limit
- Web Developer Handbook with a Getting Started guide for `educado-web`
- Back End Getting Started guide, previously an empty stub, covering local infrastructure, environment setup, the
  email worker, tests and troubleshooting

### Changed

- System Architecture rewritten against the implemented system (PostgreSQL with Sequelize, Express 5, layered API,
  Vite web app, Expo mobile app, BullMQ email pipeline, JWT role model)
- API Documentation now uses the real base URL and the routers actually mounted by the application, with Swagger
  pointed out as the canonical source
- Tools & Dependencies now lists the toolchain in use (GitHub Actions, Coolify, Nixpacks, Docker, PostgreSQL, Redis,
  MinIO, Resend, Expo/EAS, Swagger, Jest)
- Product Overview technical specifications corrected: Express 5 instead of NestJS, Vite instead of Vue.js, and
  self hosted Coolify deployment instead of generic public cloud
- Tools & Dependencies no longer presents `axios` as the web HTTP client: the web app calls the in house `fetch`
  wrapper in `src/shared/api/http.ts`, and `axios` is flagged as a declared but unused dependency. `flatpickr`
  added, since it is actually used
- System Architecture no longer claims `requireRole` standardises authorization: it guards the `/student` surface
  only, while admin access is enforced per handler through `ensureAdminRole(role)`
- API Documentation gained the multipart video part upload and the two student progress routes
- Back End Getting Started no longer implies tests live only under `src/application`, and warns that `npm run dev`
  uses inline env assignment, which fails in Windows `cmd` and PowerShell
- Deployment: `PORT` marked optional, matching its `5000` default in `src/index.ts`, and `Coolify 4.3.1` marked as
  a version observed on 2026-08-13
- Web Getting Started now describes the real anatomy of each feature directory instead of a uniform shape that no
  feature follows
- Bug report issue template now names the actual stack (Express, PostgreSQL) instead of unrelated examples
- Strapi evaluation: the "additional database" trade off no longer refers to MongoDB, and the architecture diagram
  carries a notice that it is historical

### Removed

- Content from an unrelated project in the System Architecture page (MongoDB, Vue.js, doctor and administrator
  domain models)

  Scope note: this covers the System Architecture page only. MongoDB still appears elsewhere by design, in
  `docs/assets/strapi/architecture.svg`, which is a historical artifact of the Strapi evaluation and is kept as
  drawn, with a warning on the page that renders it.

## [2.6.2] - 2025-12-02
### Added
- Added documentation for EAS Build and updating the app

## [2.6.1] - 2025-11-03
 
### Added
- Added Conventional Commits section, in workflow, with guidelines and examples

## [2.6.0] - 2025-10-28

### Added

- Added documentation for View Course Catalog

## [2.5.1] - 2025-10-16

### Added
- PBI-Implement-Student-Login-Interface.md
- PBI-Implement-Student-Registration-Interface.md

## [2.5.0] - 2025-10-15

### Changed

- New deliverables structure per application domain

## [2.4.0] - 2025-10-07

### Added

- Documentation Developer Handbook workflow guide
- Mobile Developer Handbook standards
    - Don't use `any`
    - Don't use `useCallback` or `useMemo`

### Changed

- Both `CHANGELOG.md` and `pyproject.toml` need to be updated in every PR
- Python interpreter configuration
- Mobile Developer Handbook
    - Screenshots moved to `assets/handbook/`
    - GitHub workflow screenshots and CI explanation updated

### Removed

- Separators in `README.md`

## [2.3.0] - 2025-10-07

### Added

- `CHANGELOG.md`
- GitHub workflows

### Fixed

- `repo_url` in `mkdocs.yml`

## [2.2.0] - 2025-10-03

### Added

- Mobile Developer Handbook

## [2.1.0] - 2025-09-22

### Added

- Strapi research
- Mobile upgrade to Expo 54 research
- SMS provider research

## [2.0.0] - 2025-09-18

### Changed

- Refactored Project section
- Refactored Backlog section

## [1.4.0] - 2025-06-09

### Changed

- Product Overview
- MVP definition
- Database Schema
- Wiki
- Project/Overview
- Project/Objectives
- Deliverables
- Tools
- API Schema

## [1.3.0] - 2025-06-02

### Added

- New PDF classification tool

## [1.2.0] - 2025-05-29

### Changed

- Refactored Backlog and create US

## [1.1.0] - 2025-05-14

### Added

- Wiki references

## [1.0.0] - 2025-05-13

### Added

- Completed all sections and added US
- Added Content QA information and minor adjustments
- Project Overview update content
- Objectives update content
- `site_url` and `repo_name` in `mkdocs.yml`

## [0.3.0] - 2025-04-18

### Changed

- Update home page

## [0.2.0] - 2025-04-15

### Changed

- Product Overview update content

## [0.1.0] - 2025-03-28

### Added

- Created the project
