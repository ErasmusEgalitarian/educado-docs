# Security Policy

Educado is an educational platform for waste pickers in Brazil, run as a
partnership between the University of Brasilia (UnB) and Aalborg University.
This repository holds the project's documentation site: a static
[MkDocs](https://www.mkdocs.org/) build with no backend, no database and no
authentication. Its attack surface is much smaller than the application
repositories (`educado-api`, `educado-web`, `educado-app`), but we still take
reports seriously, especially anything to do with the build pipeline or the
published site.

## Supported versions

Only the code on the `main` branch, and the site currently published at
https://erasmusegalitarian.github.io/educado-docs/, receive fixes. There are
no long-lived release branches and no backports to older tags.

| Version | Supported |
| ------- | --------- |
| `main` (latest) | Yes |
| Anything older | No |

## Reporting a vulnerability

Do not open a public GitHub issue, pull request or discussion for a security
vulnerability.

Report it privately by email to **190091681@aluno.unb.br**. If you prefer, you
can also use GitHub's private vulnerability reporting on this repository
(Security tab, "Report a vulnerability").

Please include, as far as you can:

- A description of the vulnerability and its impact.
- The affected file, page or build step.
- Steps to reproduce.
- The version or commit hash you tested against.
- Any logs, screenshots or proof of concept you have.
- How you would like to be credited, if you want credit.

## What to expect

This is an academic project maintained by students and researchers, so
response times can stretch during exam periods and university holidays. We
will tell you if that happens.

| Stage | Target |
| ----- | ------ |
| Acknowledgement of your report | within 5 business days |
| Initial assessment and severity triage | within 10 business days |
| Fix for a critical or high severity issue | within 30 days of triage |
| Fix for medium or low severity | scheduled into the normal release flow |

If we accept the report, we will work on a fix, keep you updated, and credit
you in the release notes unless you ask us not to. If we decline it, we will
explain why. Please keep the details private until a fix is released.

## Scope

In scope:

- The source code in this repository: the MkDocs configuration
  (`mkdocs.yml`), the `parse_files.py` release script, the GitHub Actions
  workflows in `.github/workflows/`, and the documentation content itself.
- The published site at https://erasmusegalitarian.github.io/educado-docs/,
  for issues such as content injection through the build (e.g. unsanitized
  Markdown or plugin output that executes script in a reader's browser) or
  supply-chain problems in the build (compromised dependency, workflow
  injection, secrets exposed in CI logs or artifacts).
- Secrets, credentials or personal data accidentally committed to this
  repository.

Out of scope:

- The backend API, the web frontend and the mobile app. Report those against
  `educado-api`, `educado-web` or `educado-app` respectively; this repository
  ships no runtime application code and holds no user data.
- Denial of service or volumetric load testing against GitHub Pages.
- Broken links, typos, outdated screenshots or other purely editorial issues:
  please open a normal issue for those, not a security report.
- Reports produced only by an automated scanner, with no demonstrated impact.
- Missing hardening headers on GitHub Pages, since we do not control that
  infrastructure. Report those to GitHub instead.
- Third party services we do not operate (GitHub Pages, GitHub Actions).
  Report those to the vendor.

## Testing guidelines

If you test against the published site or the CI pipeline, do not run
destructive operations, do not attempt to exfiltrate CI secrets, and stop as
soon as you have confirmed the issue. A minimal proof of concept is enough to
demonstrate impact.
