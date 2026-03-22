#!/bin/bash
echo "============================================"
echo " QuantiesUnite Learning Platform"
echo " Starting local server..."
echo "============================================"

cd "$(dirname "$0")"

pip show flask > /dev/null 2>&1 || pip install flask waitress

echo "Server starting at: http://localhost:5001"
python3 app.py
