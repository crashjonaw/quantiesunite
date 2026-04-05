#!/bin/bash
echo "================================================"
echo "  Bloom Bar - Diagnostics"
echo "================================================"
echo ""

SCRIPT_DIR="$(dirname "$0")"

echo "[1] Checking Python..."
if python3 --version 2>/dev/null; then
    echo "OK"
else
    echo "FAIL: Python not found (install via: brew install python)"
fi

echo ""
echo "[2] Checking pip..."
if pip3 --version 2>/dev/null; then
    echo "OK"
else
    echo "FAIL: pip not found"
fi

echo ""
echo "[3] Checking ngrok..."
if which ngrok 2>/dev/null; then
    echo "OK: $(which ngrok)"
else
    echo "FAIL: ngrok not found (install with: brew install ngrok/ngrok/ngrok)"
fi

echo ""
echo "[4] Checking cloudflared..."
if which cloudflared 2>/dev/null; then
    echo "OK: $(which cloudflared)"
else
    echo "WARN: cloudflared not found (install with: brew install cloudflared)"
fi

echo ""
echo "[5] Checking Flask install..."
if python3 -c "import flask; print('Flask', flask.__version__)"; then
    echo "OK"
else
    echo "FAIL: Flask not installed (run: pip3 install flask)"
fi

echo ""
echo "[6] Checking gunicorn install..."
if which gunicorn 2>/dev/null; then
    echo "OK: $(which gunicorn)"
else
    echo "FAIL: gunicorn not found (run: pip3 install gunicorn)"
fi

echo ""
echo "[7] Checking project files..."
if [ -f "$SCRIPT_DIR/app.py" ]; then echo "OK: app.py found"; else echo "FAIL: app.py missing"; fi
if [ -f "$SCRIPT_DIR/.env" ]; then echo "OK: .env found"; else echo "WARN: .env missing"; fi

echo ""
echo "================================================"
echo "  Done. Screenshot this window and share it."
echo "================================================"
