#!/usr/bin/env bash
set -euo pipefail

upstream_url="${PAPER_NOTES_UPSTREAM_URL:-https://github.com/zhaoyang97/Paper-Notes.git}"
upstream_branch="${PAPER_NOTES_UPSTREAM_BRANCH:-main}"
target_dir="${1:-docs}"
cache_dir="${PAPER_NOTES_CACHE_DIR:-.cache/Paper-Notes-upstream}"
state_file="${PAPER_NOTES_STATE_FILE:-data/provenance/PAPER_NOTES_UPSTREAM.md}"
manifest_file="${PAPER_NOTES_MANIFEST_FILE:-data/provenance/PAPER_NOTES_UPSTREAM_DIRS.txt}"
license_file="${PAPER_NOTES_LICENSE_FILE:-third_party/Paper-Notes/LICENSE}"
max_file_bytes="${PAPER_NOTES_MAX_FILE_BYTES:-99614720}"
max_total_bytes="${PAPER_NOTES_MAX_TOTAL_BYTES:-1073741824}"
force_sync="${PAPER_NOTES_FORCE_SYNC:-0}"

conference_dir_pattern='^[A-Za-z][A-Za-z0-9_-]*[0-9]{4}$'

fail() {
  echo "Paper-Notes sync refused: $*" >&2
  exit 1
}

validate_relative_path() {
  local label="$1"
  local value="$2"
  case "$value" in
    ""|"."|"/"|/*|*".."*)
      fail "$label must be a non-empty repository-relative path: $value"
      ;;
  esac
}

validate_non_negative_integer() {
  local label="$1"
  local value="$2"
  if ! [[ "$value" =~ ^[0-9]+$ ]]; then
    fail "$label must be a non-negative integer"
  fi
}

validate_relative_path "target_dir" "$target_dir"
validate_relative_path "state_file" "$state_file"
validate_relative_path "manifest_file" "$manifest_file"
validate_relative_path "license_file" "$license_file"
validate_non_negative_integer "PAPER_NOTES_MAX_FILE_BYTES" "$max_file_bytes"
validate_non_negative_integer "PAPER_NOTES_MAX_TOTAL_BYTES" "$max_total_bytes"

remote_revision="$(
  git ls-remote "$upstream_url" "refs/heads/$upstream_branch" |
    awk 'NR == 1 { print $1 }'
)"
if ! [[ "$remote_revision" =~ ^[0-9a-fA-F]{40}$ ]]; then
  fail "could not resolve $upstream_url branch $upstream_branch"
fi

existing_revision=""
if [ -f "$state_file" ]; then
  existing_revision="$(
    sed -n 's/^- upstream_commit: //p' "$state_file" | head -n 1
  )"
fi

if [ "$force_sync" != "1" ] && [ "$existing_revision" = "$remote_revision" ]; then
  echo "Paper-Notes docs are already current at $remote_revision"
  exit 0
fi

mkdir -p "$(dirname "$cache_dir")"
if [ -d "$cache_dir/.git" ]; then
  git -C "$cache_dir" remote set-url origin "$upstream_url"
  git -C "$cache_dir" fetch --depth=1 origin "$upstream_branch"
else
  git clone \
    --depth=1 \
    --filter=blob:none \
    --no-checkout \
    --branch "$upstream_branch" \
    "$upstream_url" \
    "$cache_dir"
  git -C "$cache_dir" sparse-checkout init --cone
fi

git -C "$cache_dir" sparse-checkout set docs
if ! git -C "$cache_dir" cat-file -e "${remote_revision}^{commit}" 2>/dev/null; then
  git -C "$cache_dir" fetch --depth=1 origin "$remote_revision"
fi
git -C "$cache_dir" checkout --detach "$remote_revision"

resolved_revision="$(git -C "$cache_dir" rev-parse HEAD)"
if [ "$resolved_revision" != "$remote_revision" ]; then
  fail "checked out $resolved_revision but expected $remote_revision"
fi
if [ ! -d "$cache_dir/docs" ] || [ ! -f "$cache_dir/LICENSE" ]; then
  fail "upstream must contain docs/ and LICENSE"
fi
if find "$cache_dir/docs" -type l -print -quit | grep -q .; then
  fail "upstream docs must not contain symbolic links"
fi

staging_dir="$(mktemp -d "${TMPDIR:-/tmp}/paper-notes-docs-sync.XXXXXX")"
cleanup() {
  rm -rf -- "$staging_dir"
}
trap cleanup EXIT

mkdir -p "$staging_dir/docs"
new_manifest="$staging_dir/PAPER_NOTES_UPSTREAM_DIRS.txt"
: > "$new_manifest"

while IFS= read -r -d '' source_dir; do
  name="$(basename "$source_dir")"
  if ! [[ "$name" =~ $conference_dir_pattern ]]; then
    continue
  fi
  printf '%s\n' "$name" >> "$new_manifest"
  mkdir -p "$staging_dir/docs/$name"
  rsync -a --delete "$source_dir/" "$staging_dir/docs/$name/"
done < <(
  find "$cache_dir/docs" -mindepth 1 -maxdepth 1 -type d -print0 |
    sort -z
)

sort -u -o "$new_manifest" "$new_manifest"
if [ ! -s "$new_manifest" ]; then
  fail "no conference-year directories matched $conference_dir_pattern"
fi

total_bytes=0
while IFS= read -r -d '' file; do
  size="$(wc -c < "$file" | tr -d '[:space:]')"
  if [ "$size" -gt "$max_file_bytes" ]; then
    fail "oversized file (${size} bytes): $file"
  fi
  total_bytes=$((total_bytes + size))
  if [ "$total_bytes" -gt "$max_total_bytes" ]; then
    fail "selected docs exceed total limit (${total_bytes} bytes)"
  fi
done < <(find "$staging_dir/docs" -type f -print0)

declare -A previously_managed=()
if [ -f "$manifest_file" ]; then
  while IFS= read -r old_name; do
    [ -n "$old_name" ] || continue
    if ! [[ "$old_name" =~ $conference_dir_pattern ]]; then
      fail "invalid directory in existing manifest: $old_name"
    fi
    previously_managed["$old_name"]=1
  done < "$manifest_file"
fi

while IFS= read -r new_name; do
  if [ -e "$target_dir/$new_name" ] &&
     [ -z "${previously_managed[$new_name]+managed}" ]; then
    fail "refusing to overwrite unmanaged local directory: $target_dir/$new_name"
  fi
done < "$new_manifest"

if [ -f "$manifest_file" ]; then
  while IFS= read -r old_name; do
    [ -n "$old_name" ] || continue
    if ! grep -qxF "$old_name" "$new_manifest" &&
       [ -e "$target_dir/$old_name" ]; then
      rm -rf -- "$target_dir/$old_name"
    fi
  done < "$manifest_file"
fi

mkdir -p "$target_dir"
while IFS= read -r new_name; do
  mkdir -p "$target_dir/$new_name"
  rsync -a --delete "$staging_dir/docs/$new_name/" "$target_dir/$new_name/"
done < "$new_manifest"

mkdir -p \
  "$(dirname "$state_file")" \
  "$(dirname "$manifest_file")" \
  "$(dirname "$license_file")"
cp "$new_manifest" "$manifest_file"
cp "$cache_dir/LICENSE" "$license_file"

synced_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
cat > "$state_file" <<EOF
# Paper-Notes docs provenance

- upstream_repository: $upstream_url
- upstream_branch: $upstream_branch
- upstream_commit: $remote_revision
- synced_at_utc: $synced_at
- mirrored_scope: conference-year directories from upstream docs/
- managed_directory_manifest: $manifest_file
- protected_local_paths: docs/index.md, docs/search.md, docs/notes/, docs/assets/, docs/javascripts/, docs/stylesheets/, docs/review-routing.md
- license_copy: $license_file

The synchronized conference notes originate from zhaoyang97/Paper-Notes.
Local AAMAS notes and the adapted AAMAS front end are deliberately excluded
from synchronization. Retain the upstream license and attribution.
EOF

echo "Synchronized Paper-Notes $remote_revision: $(wc -l < "$new_manifest" | tr -d '[:space:]') conference directories, $total_bytes bytes"
