#!/bin/bash

echo "🚀 Script started"

# Force tmux to use your active socket
SOCKET="$(echo "$TMUX" | cut -d',' -f1)"

# Fallback if not inside tmux
if [ -z "$SOCKET" ]; then
  SOCKET="/private/tmp/tmux-$(id -u)/default"
fi

echo "🔌 Using tmux socket: $SOCKET"

while true; do
  echo "⏳ Waiting 1 hour..."
  sleep 10   # keep short for testing (change to 3600 later)

  echo "🔍 Checking tmux session..."

  if tmux -S "$SOCKET" has-session -t claude 2>/dev/null; then
    echo "✅ Session found"

    # Capture recent output
    output=$(tmux -S "$SOCKET" capture-pane -pt claude -S -50)

    echo "📄 Captured output:"
    echo "$output"

    # Detect menu more flexibly
    if echo "$output" | grep -E "1|Resume|continue" >/dev/null; then
      echo "📋 Menu detected → sending 1 + continue"

      tmux -S "$SOCKET" send-keys -t claude "1" Enter
      sleep 1.5
      tmux -S "$SOCKET" send-keys -t claude "continue" Enter
    else
      echo "💬 Sending continue only"
      tmux -S "$SOCKET" send-keys -t claude "continue" Enter
    fi

  else
    echo "❌ tmux session 'claude' not found"
  fi

done