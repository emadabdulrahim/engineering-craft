#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf 'Usage: %s [--uninstall | --help]\n' "${0##*/}"
}

if [[ $# -gt 1 ]]; then
  usage >&2
  exit 2
fi

case "${1:-}" in
  '') mode=install ;;
  --uninstall) mode=uninstall ;;
  --help) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

if [[ "${HOME:-}" != /* || ! -d "$HOME" ]]; then
  printf 'HOME must name an existing absolute directory.\n' >&2
  exit 1
fi

root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
destinations=("$HOME/.claude/skills" "$HOME/.agents/skills")
shopt -s nullglob

if [[ "$mode" == uninstall ]]; then
  for destination in "${destinations[@]}"; do
    for target in "$destination"/*; do
      if [[ -L "$target" && "$(readlink "$target")" == "$root/skills/${target##*/}" ]]; then
        rm -- "$target"
        printf 'Removed %s\n' "$target"
      fi
    done
  done
  exit 0
fi

files=("$root"/skills/*/SKILL.md)
if [[ ${#files[@]} -eq 0 ]]; then
  printf 'No skills found in %s/skills.\n' "$root" >&2
  exit 1
fi

conflicts=0
for destination in "${destinations[@]}"; do
  for directory in "${destination%/*}" "$destination"; do
    if [[ ( -e "$directory" || -L "$directory" ) && ! -d "$directory" ]]; then
      printf 'Conflict: %s is not a directory.\n' "$directory" >&2
      conflicts=1
    fi
  done
  for file in "${files[@]}"; do
    source=${file%/SKILL.md}
    target="$destination/${source##*/}"
    if [[ -L "$target" && "$(readlink "$target")" == "$source" ]]; then
      continue
    fi
    if [[ -e "$target" || -L "$target" ]]; then
      printf 'Conflict: %s already exists and does not link to %s.\n' "$target" "$source" >&2
      conflicts=1
    fi
  done
done

if [[ "$conflicts" -ne 0 ]]; then
  printf 'Nothing installed. Resolve the conflicts and run again.\n' >&2
  exit 1
fi

for destination in "${destinations[@]}"; do
  mkdir -p -- "$destination"
  for file in "${files[@]}"; do
    source=${file%/SKILL.md}
    target="$destination/${source##*/}"
    if [[ -L "$target" && "$(readlink "$target")" == "$source" ]]; then
      printf 'Already installed: %s\n' "$target"
    else
      ln -s -- "$source" "$target"
      printf 'Installed %s -> %s\n' "$target" "$source"
    fi
  done
done
