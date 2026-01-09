#!/usr/bin/env bash
set -u

file_path="${1:-}"
if [ -z "$file_path" ]; then
  read -r file_path || true
fi

if [ -z "$file_path" ]; then
  exit 0
fi

if [ ! -f "$file_path" ]; then
  exit 0
fi

case "$file_path" in
  */test/*_test.rb) test_type="minitest" ;;
  *) exit 0 ;;
esac

project_dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"

if [ ! -f "${project_dir}/Gemfile" ]; then
  exit 0
fi

if [ "$test_type" = "minitest" ]; then
  if [ -x "${project_dir}/bin/rails" ]; then
    (cd "$project_dir" && bin/rails test "$file_path")
    exit $?
  fi
  if command -v bundle >/dev/null 2>&1 && (cd "$project_dir" && bundle exec rails -v >/dev/null 2>&1); then
    (cd "$project_dir" && bundle exec rails test "$file_path")
    exit $?
  fi
fi

exit 0
