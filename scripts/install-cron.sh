#!/bin/bash
# Install the daily Kinsta docs sync into the current user's crontab.
#
# Everything is derived at runtime: the skill directory from this script's own
# location, and python3 from PATH (override with PYTHON=/path/to/python3).
# Nothing about one particular machine is baked in.
#
# Idempotent: safe to run repeatedly, and safe to call from a startup script on
# a platform that does not persist crontabs across reboots.
#
#   bash install-cron.sh          # install or refresh
#   bash install-cron.sh --check  # report state, change nothing
#   bash install-cron.sh --remove # uninstall

set -uo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$SKILL_DIR/scripts/kinsta_kb.py"
LOGFILE="$SKILL_DIR/kb/cron.log"
MARKER="# kinsta-docs mirror sync (managed by install-cron.sh)"

# cron runs with a minimal PATH, so the interpreter goes in by absolute path.
# Resolve it now rather than assuming where python3 lives on this platform.
PYTHON="${PYTHON:-$(command -v python3 || true)}"
if [[ -z "$PYTHON" ]]; then
  echo "FAIL: no python3 on PATH. Set PYTHON=/path/to/python3 and re-run." >&2
  exit 1
fi
PYTHON="$(cd "$(dirname "$PYTHON")" && pwd)/$(basename "$PYTHON")"

# 04:17 rather than on the hour, so this does not pile up with every other job
# that fires at :00.
LINE="17 4 * * * $PYTHON $SCRIPT sync >> $LOGFILE 2>&1"

mode="install"
case "${1:-}" in
  --check)  mode="check" ;;
  --remove) mode="remove" ;;
  "")       ;;
  *)        echo "usage: $0 [--check|--remove]" >&2; exit 2 ;;
esac

if [[ ! -f "$SCRIPT" ]]; then
  echo "FAIL: $SCRIPT not found. Wrong directory, or the skill is not installed." >&2
  exit 1
fi
if ! "$PYTHON" -c "import requests, bs4, markdownify" 2>/dev/null; then
  echo "FAIL: $PYTHON is missing one of requests / beautifulsoup4 / markdownify." >&2
  echo "      The cron would run and fail silently every night. Fix this first:" >&2
  echo "      $PYTHON -m pip install requests beautifulsoup4 markdownify PyYAML" >&2
  exit 1
fi
if ! command -v crontab >/dev/null 2>&1; then
  echo "FAIL: no crontab command on this system. Schedule this line with whatever" >&2
  echo "      scheduler you do have (launchd, systemd timer, Task Scheduler):" >&2
  echo "      $PYTHON $SCRIPT sync >> $LOGFILE 2>&1" >&2
  exit 1
fi

current="$(crontab -l 2>/dev/null || true)"

if [[ "$mode" == "check" ]]; then
  if grep -Fq "$SCRIPT sync" <<<"$current"; then
    echo "INSTALLED:"
    grep -F "$SCRIPT sync" <<<"$current" | sed 's/^/  /'
  else
    echo "NOT INSTALLED - the mirror is not being refreshed on a schedule."
    echo "The line that would be installed:"
    echo "  $LINE"
  fi
  echo
  echo "Last sync according to the mirror itself:"
  "$PYTHON" "$SCRIPT" status 2>/dev/null | sed -n '1,12p' | sed 's/^/  /'
  exit 0
fi

# Strip any previous version of our entry (and its marker) before rewriting, so
# repeated runs cannot stack duplicates. Matching on the script path rather than
# the whole line means a schedule change here still replaces the old entry
# instead of adding a second one.
cleaned="$(grep -vF -e "$MARKER" -e "$SCRIPT sync" <<<"$current" || true)"

if [[ "$mode" == "remove" ]]; then
  printf '%s\n' "$cleaned" | grep -v '^$' | crontab -
  echo "Removed. The mirror will now only be refreshed by hand or by \`check\`."
  exit 0
fi

mkdir -p "$(dirname "$LOGFILE")"
{
  printf '%s\n' "$cleaned" | grep -v '^$'
  printf '%s\n' "$MARKER"
  printf '%s\n' "$LINE"
} | crontab -

echo "Installed into the $(whoami) crontab:"
echo "  $LINE"
echo
echo "Verify it is really there - a crontab write can be rejected silently:"
echo "  crontab -l | grep kinsta"
echo
if ! crontab -l 2>/dev/null | grep -Fq "$SCRIPT sync"; then
  echo "WARNING: the entry is NOT in the crontab after writing it. Something" >&2
  echo "         rejected the write. Do not assume this is scheduled." >&2
  exit 1
fi
echo "Confirmed present."
echo
echo "On most systems the crontab persists across reboots and you are done."
echo "If yours does not - a crontab on a RAM disk or tmpfs, a container rebuilt"
echo "from an image, an appliance OS that restores state at boot - call this"
echo "script from that platform's startup mechanism. It is idempotent."
echo
echo "On macOS, cron and launchd jobs may need Full Disk Access before they can"
echo "write under your home directory. Check kb/cron.log after the first run."
