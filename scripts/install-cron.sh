#!/bin/bash
# Install the daily Kinsta docs sync into the `tim` crontab.
#
# Idempotent: safe to run repeatedly, and safe to call from the boot chain.
# It must be called from the boot chain, because crontabs on this box live on
# the root RAM disk and do not survive a reboot. A cron that works today and
# silently disappears on the next reboot is worse than no cron at all, because
# `status` keeps reporting a once-fresh mirror while it drifts.
#
#   bash install-cron.sh          # install or refresh
#   bash install-cron.sh --check  # report state, change nothing
#   bash install-cron.sh --remove # uninstall

set -uo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$SKILL_DIR/scripts/kinsta_kb.py"
LOGFILE="$SKILL_DIR/kb/cron.log"
MARKER="# kinsta-docs mirror sync (managed by install-cron.sh)"
# 04:17 rather than on the hour, so this does not pile up with every other job
# that fires at :00.
LINE="17 4 * * * /usr/bin/python3 $SCRIPT sync >> $LOGFILE 2>&1"

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
if ! /usr/bin/python3 -c "import requests, bs4, markdownify, yaml" 2>/dev/null; then
  echo "FAIL: python3 is missing one of requests / bs4 / markdownify / yaml." >&2
  echo "      The cron would run and fail silently every night. Fix this first." >&2
  exit 1
fi

current="$(crontab -l 2>/dev/null || true)"

if [[ "$mode" == "check" ]]; then
  if grep -Fq "$SCRIPT sync" <<<"$current"; then
    echo "INSTALLED:"
    grep -F "$SCRIPT sync" <<<"$current" | sed 's/^/  /'
  else
    echo "NOT INSTALLED - the mirror is not being refreshed on a schedule."
  fi
  echo
  echo "Last sync according to the mirror itself:"
  /usr/bin/python3 "$SCRIPT" status 2>/dev/null | sed -n '1,12p' | sed 's/^/  /'
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
echo "Verify it is really there (this is the check that matters - a silent"
echo "crontab write is a known failure mode on this box):"
echo "  crontab -l | grep kinsta"
echo
if ! crontab -l 2>/dev/null | grep -Fq "$SCRIPT sync"; then
  echo "WARNING: the entry is NOT in the crontab after writing it. Something" >&2
  echo "         rejected the write. Do not assume this is scheduled." >&2
  exit 1
fi
echo "Confirmed present."
echo
echo "Boot persistence: crontabs here live on the root RAM disk, so add a call"
echo "to this script in the boot chain (/boot/config/go ->"
echo "restore-persistence.sh) if it is not already there:"
echo "  grep -rn install-cron.sh /boot/config/ 2>/dev/null"
