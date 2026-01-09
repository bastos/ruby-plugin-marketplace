#!/usr/bin/env bash
set -u

file_path="${1:-}"
if [ -z "$file_path" ]; then
  read -r file_path || true
fi

if [ -z "$file_path" ]; then
  exit 0
fi

case "$file_path" in
  *.rb|*.rake|*.ru|Gemfile|Rakefile) ;;
  *) exit 0 ;;
esac

project_dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"

if [ ! -f "${project_dir}/Gemfile" ]; then
  exit 0
fi

if ! command -v bundle >/dev/null 2>&1; then
  exit 0
fi

if ! (cd "$project_dir" && bundle exec rubocop -v >/dev/null 2>&1); then
  exit 0
fi

(cd "$project_dir" && bundle exec rubocop -A --force-exclusion "$file_path") || true
