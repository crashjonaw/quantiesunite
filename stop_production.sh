#!/usr/bin/env bash
# Stop QuantiesUnite production processes and close Terminal windows

cd "$(dirname "$0")"

echo "Stopping QuantiesUnite..."

# Kill processes
pkill -f "cloudflared.*quantiesunite" 2>/dev/null && echo "  Cloudflare Tunnel stopped" || echo "  Tunnel was not running"
# Only kill gunicorn on port 5001 (don't kill other apps like bloomburrow on 5000)
lsof -ti:5001 | xargs kill -9 2>/dev/null && echo "  Gunicorn stopped" || echo "  Gunicorn was not running"

# Close the QU-Gunicorn and QU-Tunnel Terminal windows
osascript -e '
tell application "Terminal"
    repeat with w in windows
        try
            if custom title of w is "QU-Gunicorn" or custom title of w is "QU-Tunnel" then
                close w saving no
            end if
        end try
    end repeat
end tell
' 2>/dev/null

# Clean up PID files
rm -f logs/gunicorn.pid logs/cloudflared.pid 2>/dev/null

echo "Done."
