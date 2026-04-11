#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
#  QuantiesUnite — Production Launch Script
#
#  Usage:
#    First time:  chmod +x run_production.sh && ./run_production.sh
#    After that:  ./run_production.sh
#
#  This script will:
#    1. Check Python and dependencies
#    2. Generate a SECRET_KEY if not set
#    3. Create/load .env file
#    4. Back up the database
#    5. Initialise the database (if fresh)
#    6. Launch gunicorn for production
# ═══════════════════════════════════════════════════════════════════

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# ── Colors ──────────────────────────────────────────────────────────
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

info()  { echo -e "${CYAN}[INFO]${NC}  $1"; }
ok()    { echo -e "${GREEN}[OK]${NC}    $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $1"; }
fail()  { echo -e "${RED}[FAIL]${NC}  $1"; exit 1; }

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  QuantiesUnite — Production Launcher"
echo "═══════════════════════════════════════════════════════════"
echo ""

# ── 1. Check Python ─────────────────────────────────────────────────
info "Checking Python..."
PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        PYTHON="$cmd"
        break
    fi
done
[ -z "$PYTHON" ] && fail "Python not found. Install Python 3.8+."
PY_VER=$($PYTHON --version 2>&1)
ok "Found $PY_VER"

# ── 2. Check/install dependencies ───────────────────────────────────
info "Checking dependencies..."
if [ -f requirements.txt ]; then
    $PYTHON -m pip install -q -r requirements.txt 2>/dev/null || {
        warn "pip install had issues — trying with --user flag"
        $PYTHON -m pip install -q --user -r requirements.txt
    }
    ok "Dependencies installed"
else
    warn "No requirements.txt found — skipping"
fi

# Check gunicorn specifically
if ! $PYTHON -c "import gunicorn" 2>/dev/null; then
    fail "gunicorn not installed. Run: pip install gunicorn"
fi
ok "gunicorn available"

# ── 3. Environment file (.env) ──────────────────────────────────────
info "Checking .env configuration..."
if [ ! -f .env ]; then
    warn ".env not found — creating with generated SECRET_KEY"
    SECRET_KEY=$($PYTHON -c "import secrets; print(secrets.token_hex(32))")
    cat > .env << ENVEOF
# QuantiesUnite Production Environment
# Generated on $(date '+%Y-%m-%d %H:%M:%S')

# Flask secret key — DO NOT SHARE, DO NOT COMMIT
SECRET_KEY=$SECRET_KEY

# Server binding (127.0.0.1 — cloudflared tunnels to this)
GUNICORN_BIND=127.0.0.1:5001

# Workers & threads (auto-detected if not set)
# GUNICORN_WORKERS=5
# GUNICORN_THREADS=4

# Log level: debug, info, warning, error
GUNICORN_LOGLEVEL=info
ENVEOF
    ok "Created .env with a secure SECRET_KEY"
else
    ok ".env already exists"
fi

# Load .env into current shell
set -a
source .env
set +a
ok "Environment loaded"

# Verify SECRET_KEY is set
if [ -z "$SECRET_KEY" ]; then
    fail "SECRET_KEY is empty in .env — please set a value"
fi
ok "SECRET_KEY is set (${#SECRET_KEY} chars)"

# ── 4. Check Google OAuth credentials ──────────────────────────────
info "Checking Google OAuth..."
if [ -f google_api_secret.json ]; then
    ok "google_api_secret.json found"
else
    warn "google_api_secret.json not found — Google Sign-In will be disabled"
fi

# ── 5. Database backup ──────────────────────────────────────────────
info "Database backup..."
mkdir -p backups
if [ -f quantiesunite.db ]; then
    BACKUP_NAME="backups/quantiesunite_$(date '+%Y%m%d_%H%M%S').db"
    cp quantiesunite.db "$BACKUP_NAME"
    ok "Backed up to $BACKUP_NAME"

    # Keep only last 10 backups
    ls -t backups/quantiesunite_*.db 2>/dev/null | tail -n +11 | xargs rm -f 2>/dev/null || true
else
    info "No existing database — will be created on first run"
fi

# ── 6. Create required directories ──────────────────────────────────
mkdir -p static/uploads/avatars
mkdir -p logs
ok "Directories ready"

# ── 7. Quick sanity check ──────────────────────────────────────────
info "Running sanity check..."
$PYTHON -c "
import app
import database as db
from curriculum_data import TOPICS
print(f'  Modules loaded: {len(TOPICS)}')
count = db.get_db().execute('SELECT COUNT(*) AS c FROM quiz_questions').fetchone()['c']
print(f'  Quiz questions in DB: {count}')
exam_count = db.get_db().execute('SELECT COUNT(*) AS c FROM exam_questions').fetchone()['c']
print(f'  Exam questions in DB: {exam_count}')
users = db.get_db().execute('SELECT COUNT(*) AS c FROM users').fetchone()['c']
print(f'  Registered users: {users}')
" || fail "Sanity check failed — fix errors above before launching"
ok "Sanity check passed"

# ── 8. Fix cloudflared config ──────────────────────────────────────
info "Checking Cloudflare Tunnel config..."
CF_CONFIG="$HOME/.cloudflared/config.yml"
if [ -f "$CF_CONFIG" ]; then
    sed -i '' 's/localhost:5001/127.0.0.1:5001/g' "$CF_CONFIG" 2>/dev/null || true
    ok "cloudflared config patched (localhost → 127.0.0.1)"
else
    warn "No cloudflared config found at $CF_CONFIG"
fi

# ── 9. Clean up old processes ─────────────────────────────────────
info "Cleaning up old processes..."
lsof -ti:5001 | xargs kill -9 2>/dev/null || true
pkill -f "cloudflared.*quantiesunite" 2>/dev/null || true
pkill -f "gunicorn.*app:app" 2>/dev/null || true
sleep 2
ok "Old processes cleaned"

# ── 10. Launch ──────────────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════════════════════"
echo -e "  ${GREEN}Launching QuantiesUnite in production mode${NC}"
echo "  Gunicorn: ${GUNICORN_BIND:-127.0.0.1:5001}"
echo "  Tunnel:   https://quantiesunite.sg"
echo "  Logs:     logs/access.log, logs/error.log"
echo ""
echo "  Stop with: ./stop_production.sh or kill \$(cat logs/gunicorn.pid)"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Export SECRET_KEY so all gunicorn workers inherit the same key
export SECRET_KEY

# Start gunicorn in a new Terminal window
info "Starting Gunicorn..."
osascript -e "
tell app \"Terminal\"
    set w to do script \"cd '$SCRIPT_DIR' && export SECRET_KEY='$SECRET_KEY' && gunicorn -c gunicorn.conf.py app:app\"
    set custom title of window 1 to \"QU-Gunicorn\"
end tell"

echo "Waiting for Gunicorn to start..."
sleep 5

if curl -s -o /dev/null -w '' http://127.0.0.1:5001/ 2>/dev/null; then
    ok "Gunicorn is running on 127.0.0.1:5001"
else
    warn "Gunicorn may still be starting — check the QU-Gunicorn terminal"
fi

# Start Cloudflare Tunnel in a new Terminal window
info "Starting Cloudflare Tunnel..."
osascript -e "
tell app \"Terminal\"
    set w to do script \"cloudflared tunnel run --url http://127.0.0.1:5001 quantiesunite\"
    set custom title of window 1 to \"QU-Tunnel\"
end tell"

sleep 3
ok "Cloudflare Tunnel launched"

echo ""
echo "═══════════════════════════════════════════════════════════"
echo -e "  ${GREEN}QuantiesUnite is live!${NC}"
echo ""
echo "  Local:   http://localhost:5001"
echo "  Public:  https://quantiesunite.sg"
echo ""
echo "  Gunicorn running in Terminal: QU-Gunicorn"
echo "  Tunnel   running in Terminal: QU-Tunnel"
echo "  Stop by closing those terminal windows"
echo "═══════════════════════════════════════════════════════════"
echo ""
