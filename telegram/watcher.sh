#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# QuantiesUnite Telegram Watcher
# Polls Telegram for admin commands and runs Claude Code tasks
#
# Usage:
#   nohup ./telegram/watcher.sh &
#
# Telegram commands (from @crashjaw):
#   "status"        — reply with current status
#   "claude:{msg}"  — forward message to Claude as a one-off task
#   "redeploy"      — kill server on port 5001 and redeploy via run.sh
# ═══════════════════════════════════════════════════════════════

BOT_TOKEN="8788896345:AAFCIAPnGdThrCouP95q5x1ZP-qZEaldmac"
CHAT_ID="86480008"
ADMIN_USERNAME="crashjaw"
PROJECT_DIR="/Users/crashjonaw/Desktop/quantiesunite"
POLL_INTERVAL=30
OFFSET=0

INBOX_FILE="${PROJECT_DIR}/telegram/inbox.txt"
TASK_PID=""

send_telegram() {
    local text="$1"
    curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
        -H "Content-Type: application/json" \
        -d "{\"chat_id\":\"${CHAT_ID}\",\"text\":\"${text}\",\"parse_mode\":\"Markdown\"}" > /dev/null 2>&1
}

PROMPT_FILE="${PROJECT_DIR}/telegram/loop_prompt.txt"
FIX_PID=""

run_fix() {
    # Kill any existing fix run
    if [ -n "$FIX_PID" ] && kill -0 "$FIX_PID" 2>/dev/null; then
        kill "$FIX_PID" 2>/dev/null
        wait "$FIX_PID" 2>/dev/null
    fi
    cd "$PROJECT_DIR"
    FULL_PROMPT=$(cat "$PROMPT_FILE")
    claude --dangerously-skip-permissions -p "$FULL_PROMPT" &
    FIX_PID=$!
    echo "[watcher] Fix started with PID $FIX_PID"
    send_telegram "Fix started (PID: $FIX_PID) — scanning feedback CSV for unfixed issues."
}

echo "[watcher] QuantiesUnite Telegram Watcher started"
echo "[watcher] Polling every ${POLL_INTERVAL}s for commands from @${ADMIN_USERNAME}"
send_telegram "Watcher started. Commands: *fix*, *status*, *redeploy*, *claude:{msg}*"

while true; do
    # Fetch updates from Telegram
    RESPONSE=$(curl -s "https://api.telegram.org/bot${BOT_TOKEN}/getUpdates?offset=${OFFSET}&timeout=0" 2>/dev/null)

    if [ -z "$RESPONSE" ]; then
        sleep "$POLL_INTERVAL"
        continue
    fi

    # Parse updates and handle commands using python
    TMPFILE=$(mktemp)
    echo "$RESPONSE" > "$TMPFILE"

    RESULT=$(RESP_FILE="$TMPFILE" INBOX_FILE="$INBOX_FILE" ADMIN_USER="$ADMIN_USERNAME" python3 << 'PYEOF'
import json, os, sys

response_file = os.environ.get("RESP_FILE", "")
inbox_file = os.environ.get("INBOX_FILE", "")
admin = os.environ.get("ADMIN_USER", "")

with open(response_file) as f:
    data = json.load(f)

last_id = 0
for u in data.get("result", []):
    last_id = u["update_id"]
    msg = u.get("message", {})
    user = msg.get("from", {}).get("username", "")
    text = msg.get("text", "")
    if user != admin or not text:
        print(f"OFFSET:{last_id}")
        continue

    cmd = text.strip().lower()

    if cmd == "fix":
        print(f"OFFSET:{last_id}")
        print("CMD:fix")
    elif cmd == "status":
        print(f"OFFSET:{last_id}")
        print("CMD:status")
    elif cmd == "redeploy":
        print(f"OFFSET:{last_id}")
        print("CMD:redeploy")
    elif cmd.startswith("claude:"):
        forwarded = text[7:].strip()
        if inbox_file and forwarded:
            from datetime import datetime
            with open(inbox_file, "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {forwarded}\n")
        print(f"OFFSET:{last_id}")
        print("CMD:claude")
    else:
        print(f"OFFSET:{last_id}")
        print("CMD:unknown")
PYEOF
    )

    rm -f "$TMPFILE"

    while IFS= read -r line; do
        case "$line" in
            OFFSET:*)
                OFFSET=$(( ${line#OFFSET:} + 1 ))
                ;;
            CMD:fix)
                echo "[watcher] Admin requested: fix"
                run_fix
                ;;
            CMD:status)
                STATUS_MSG=""
                if [ -n "$FIX_PID" ] && kill -0 "$FIX_PID" 2>/dev/null; then
                    STATUS_MSG="Fix is *running* (PID: $FIX_PID)"
                else
                    STATUS_MSG="No fix running."
                fi
                if [ -n "$TASK_PID" ] && kill -0 "$TASK_PID" 2>/dev/null; then
                    STATUS_MSG="${STATUS_MSG}\nClaude task *running* (PID: $TASK_PID)"
                fi
                send_telegram "$STATUS_MSG"
                ;;
            CMD:redeploy)
                echo "[watcher] Admin requested: redeploy"
                send_telegram "Redeploying server..."
                osascript -e 'tell application "Terminal" to close (every window whose busy is false)' 2>/dev/null
                lsof -ti:5001 | xargs kill -9 2>/dev/null
                sleep 2
                cd "$PROJECT_DIR" && bash run.sh
                send_telegram "Server redeployed."
                ;;
            CMD:claude)
                CLAUDE_MSG=$(tail -1 "$INBOX_FILE" | sed 's/^\[.*\] //')
                echo "[watcher] Claude task: $CLAUDE_MSG"
                cd "$PROJECT_DIR"
                if [ -n "$TASK_PID" ] && kill -0 "$TASK_PID" 2>/dev/null; then
                    send_telegram "Sent to existing Claude task instance (PID: $TASK_PID)."
                else
                    send_telegram "Launching new Claude task instance..."
                    claude --dangerously-skip-permissions -p "Read documentation/project-summary.md and update/rules.md and update/notes.md for context. Then do the following: $CLAUDE_MSG. When done, send a Telegram notification via: python3 -c \"from telegram.notify import send_message; send_message('Task complete.')\"" &
                    TASK_PID=$!
                    echo "[watcher] Claude task started with PID $TASK_PID"
                    send_telegram "Claude task started (PID: $TASK_PID)."
                fi
                ;;
            CMD:unknown)
                send_telegram "Unknown command. Available: *fix*, *status*, *redeploy*, *claude:{msg}*"
                ;;
        esac
    done <<< "$RESULT"

    sleep "$POLL_INTERVAL"
done
