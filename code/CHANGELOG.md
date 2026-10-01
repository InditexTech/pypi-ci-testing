<!--
SPDX-FileCopyrightText: INDUSTRIA DE DISEÑO TEXTIL S.A. (INDITEX S.A.)

SPDX-License-Identifier: Apache-2.0
-->

# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.8.4] - 2026-10-01

## [0.8.3] - 2026-09-30

## [0.8.2] - 2026-09-30

### Changed

- Restore the governed workflow files to the sync-manifest recorded revisions.
- CI: restore the governed release caller to its recorded digest so SYNC can forward the organization GPG secrets.

## [0.8.1] - 2026-09-30

### Changed

- CI: stop dependabot from editing governed workflows (prevents managed-file drift freeze).

- CI: group `github/codeql-action` dependabot bumps so `init`/`analyze` move together.

### Dependencies

- Bump dev deps: ruff 0.16.8 and ty 0.0.82 with a matching `uv.lock` regeneration
  (the dependabot pip ecosystem does not update the lockfile).

### Changed

- Enable scheduled dependency updates for the canary and its workflows.

## [0.7.1] - 2026-09-16

## [0.6.1] - 2026-09-11

## [0.5.1] - 2026-09-04

### Fixed

- chore: remove drifted managed files so governance can materialize the golden workflows

### Changed

- Migrate the Python type-checker from pyright to Astral ty.

## [0.2.0] - 2026-08-28

### Added

- Validate the real PyPI publish and GitHub Release lane end-to-end after registering the pypi.org trusted publisher.

## [0.1.0] - 2026-08-28

### Added

- Validate the Python archetype release lane end-to-end: prepare-release, PyPI publish, and GitHub release.

### Changed

### Fixed

[Unreleased]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.8.4...HEAD

[0.8.4]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.8.3...v0.8.4

[0.8.3]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.8.2...v0.8.3

[0.8.2]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.8.1...v0.8.2

[0.8.1]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.7.1...v0.8.1

[0.7.1]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.6.1...v0.7.1

[0.6.1]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.5.1...v0.6.1

[0.5.1]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.2.0...v0.5.1

[0.2.0]: https://github.com/InditexTech/pypi-ci-testing/compare/v0.1.0...v0.2.0

[0.1.0]: https://github.com/InditexTech/pypi-ci-testing/releases/tag/v0.1.0
