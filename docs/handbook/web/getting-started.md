# Web: Getting Started

This guide sets up `educado-web` for local development. The web application is the interface used by content
creators and administrators.

!!! note "No UI framework"

    `educado-web` is **plain TypeScript** bundled by Vite. There is no Vue, React or Angular. Pages are functions
    that build DOM nodes, and navigation goes through a small hand written router in `src/app/router.ts` backed by
    the History API. Do not add a framework without discussing it with the team first.

Related documents:

- [Back End Getting Started](../back-end/getting-started.md), needed because the web app talks to a running API.
- [API Documentation](../../development/technical/api.md) and the Swagger UI.
- [Deployment & Infrastructure](../../development/technical/deployment.md) for how the app is built and served in
  production.

## Prerequisites

- **Node.js 20 or newer** ([nvm](https://github.com/nvm-sh/nvm) or
  [nvm-windows](https://github.com/coreybutler/nvm-windows)).
- **Git**.
- A running Educado API, either locally on port 5001 or the deployed one.

## Clone and install

```shell
git clone git@github.com:ErasmusEgalitarian/educado-web.git
cd educado-web
npm install
```

## Environment variables

The only variable the app reads is `VITE_API_URL`, the base URL of the API. Create a `.env` in the project root:

```dotenv
VITE_API_URL=http://localhost:5001
```

If you want to work against the deployed backend instead:

```dotenv
VITE_API_URL=https://api-educado.tominho.com
```

!!! danger

    Pointing at the deployed API means you are reading and writing **live data** shared with everyone else. Prefer a
    local API while developing.

When `VITE_API_URL` is unset, `src/shared/api/http.ts` falls back to `http://localhost:5001`.

!!! important "Vite variables are compiled in"

    `import.meta.env.VITE_API_URL` is replaced at build time. Changing the value requires restarting the dev server
    (or rebuilding the image in production), not just reloading the page.

## Run the dev server

```shell
npm run dev
```

Vite serves the app at [http://localhost:3000](http://localhost:3000) (the port is pinned in `vite.config.ts`).

The dev server also proxies `/api` to `http://localhost:5001`, stripping the prefix. Note that the API client uses
`VITE_API_URL` directly, so the proxy is only a convenience for requests written against a relative `/api` path.

Make sure the API is up before you log in:

```shell
# in the educado-api checkout
docker compose up -d
npm run dev
```

## Build and preview

```shell
npm run build     # tsc type check, then vite build into dist/
npm run preview   # serve the production bundle locally
```

`npm run build` runs `tsc` first, so a type error fails the build. There is no separate type check script.

## Project structure

```text
src/
  main.ts                 entrypoint, mounts the app and wires the router
  app/
    router.ts             History API router (navigate, replace, subscribe)
    routes/               route table
    pages/                shared top level pages
    styles/globals.css    global styles
  features/
    admin/                user and institution administration
    auth/                 login, registration, password reset, profile
    courses/              course editor and management
    dashboard/            creator dashboard
    media/                upload and media library
    public/               landing and public pages
    student/              student facing pages
  shared/
    api/http.ts           fetch wrapper, ApiError, base URL
    api/auth-session.ts   access token storage
    i18n/                 pt-BR and en-US translations
    ui/                   toast, loader, language switcher
    types/                shared types
```

Feature directories share a vocabulary, not a fixed shape. The conventional meaning is `api/` for HTTP calls,
`pages/` for screens, `components/` for reusable pieces and `styles/` for CSS, but only `pages/` and `styles/`
exist in every feature. The rest are there when the feature needs them:

| Feature       | `api/` | `components/` | `pages/` | `styles/` | Extra                   |
| ------------- | :------: | :-------------: | :--------: | :---------: | ----------------------- |
| `admin`     | yes    | no            | yes      | yes       |                         |
| `auth`      | yes    | yes           | yes      | yes       |                         |
| `courses`   | yes    | no            | yes      | yes       | `editor/`, `model/` |
| `dashboard` | no     | no            | yes      | yes       |                         |
| `media`     | yes    | yes           | yes      | yes       | `services/`           |
| `public`    | no     | yes           | yes      | yes       |                         |
| `student`   | yes    | yes           | yes      | yes       |                         |

The departures are deliberate:

- `courses` is the biggest feature and splits differently: `editor/` holds the course editor and `model/` the
  domain types (`course.types.ts`) it works on. It has no `components/`.
- `media` adds `services/upload-manager.ts`, which orchestrates the chunked upload flow on top of
  `api/media.api.ts`. That is logic that fits neither a thin API module nor a page.
- `dashboard` is a single static page with its stylesheet and nothing else, so it has no `api/` and no
  `components/`.
- `public` has no `api/` of its own: the one page that needs data imports the shared client directly
  (`import { api } from '@/shared/api/http'`).
- Most features expose an `index.ts` barrel; `admin` and `dashboard` do not.

When adding a feature, reuse the vocabulary above and create only the directories you actually need. Do not add
empty `api/` or `components/` folders for the sake of symmetry.

The `@` alias resolves to `src/`, configured both in `vite.config.ts` and `tsconfig.json`.

## Talking to the API

Use the wrapper in `src/shared/api/http.ts` instead of calling `fetch` directly. It prefixes the base URL,
attaches the bearer token when `auth: true`, parses the JSON body, and throws an `ApiError` carrying `status`,
`code` and `fieldErrors` for failed responses. Clearing the session on `401` is handled there too.

## Internationalisation

Copy lives in `src/shared/i18n/index.ts` as a nested translation tree with `pt-BR` and `en-US`. The selected
language is persisted in local storage under `educado.language`. Add new strings to **both** languages: a missing
key falls back to the raw key path, which is visible to the user.

## Production build

Production uses the multi stage `Dockerfile`: Node 20 builds the bundle, nginx serves `dist/` with an SPA
fallback. `VITE_API_URL` is passed as a **build argument**, so changing the API URL requires a rebuild. Details in
[Deployment & Infrastructure](../../development/technical/deployment.md).

## Troubleshooting

| Symptom                                        | Likely cause                                                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Every request fails with a network error       | The API is not running, or `VITE_API_URL` points at the wrong port. The API default is 5001.     |
| CORS error against a local API                 | The API has `NODE_ENV=production` locally. Outside production it allows every origin.            |
| CORS error against the deployed API            | Your origin is not in the API `FRONTEND_ORIGIN` allowlist.                                      |
| Logged out on every request                    | The token expired or `ACCESS_TOKEN_SECRET` changed on the API side. Log in again.               |
| Changing `.env` has no effect                | Restart the dev server. Vite inlines the variable at build time.                                   |
| Images or videos do not load                   | Media streaming needs a valid token in the query string, and MinIO must be reachable by the API.   |
| A route renders a blank page                   | Check the browser console: the router is minimal and does not catch rendering errors for you.      |
