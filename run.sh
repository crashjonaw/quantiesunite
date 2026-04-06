#!/bin/bash
echo "====================================="
echo "  Starting QuantiesUnite"
echo "====================================="
echo ""

# Move to script directory
cd "$(dirname "$0")"
DIR="$(pwd)"

# ── Close truly idle Terminal windows (no child processes) ────────
echo "Closing idle terminal windows..."
osascript -e '
tell application "Terminal"
    repeat with w in (every window)
        try
            repeat with t in (every tab of w)
                set tabProcs to processes of t
                -- A truly idle tab only has its login shell (1 process)
                if (count of tabProcs) ≤ 1 then
                    close w saving no
                    exit repeat
                end if
            end repeat
        end try
    end repeat
end tell
' 2>/dev/null
sleep 1

# Fix cloudflared config to use 127.0.0.1 (not localhost which can resolve to IPv6)
echo "Patching cloudflared config..."
CONFIG="$HOME/.cloudflared/config.yml"
if [ -f "$CONFIG" ]; then
    sed -i '' 's/localhost:5001/127.0.0.1:5001/g' "$CONFIG"
fi

# Kill only quantiesunite's processes (by port and tunnel name)
echo "Cleaning up old processes..."
lsof -ti:5001 | xargs kill -9 2>/dev/null
pkill -f "cloudflared.*quantiesunite" 2>/dev/null
pkill -f "gunicorn.*app:app" 2>/dev/null
sleep 2

echo "Installing Python packages if needed..."
pip3 install -r requirements.txt -q
pip3 install gunicorn -q
echo ""

echo "Starting Flask server..."
osascript -e "
tell app \"Terminal\"
    set w to do script \"cd '$DIR' && gunicorn -c gunicorn.conf.py app:app\"
    set custom title of window 1 to \"QU-Gunicorn\"
end tell"

echo "Waiting for Flask to start..."
sleep 5

echo "Starting Cloudflare Tunnel..."
osascript -e "
tell app \"Terminal\"
    set w to do script \"cloudflared tunnel run --url http://127.0.0.1:5001 quantiesunite\"
    set custom title of window 1 to \"QU-Tunnel\"
end tell"

echo ""
echo "====================================="
echo "QuantiesUnite is now running."
echo "Local:   http://localhost:5001"
echo "Public:  https://quantiesunite.sg"
echo "====================================="
