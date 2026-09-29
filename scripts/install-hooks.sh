#!/bin/sh
set -eu

repo_root=$(git rev-parse --show-toplevel)
git -C "$repo_root" config core.hooksPath .githooks
printf '%s\n' 'Installed repository hooks from .githooks.'
printf '%s\n' 'The pre-commit hook will run Gitleaks against staged changes.'
