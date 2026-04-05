#!/bin/bash
echo "====================================="
echo "  Starting Bloom Bar Public Server"
echo "====================================="
echo ""

# Move to script directory
cd "$(dirname "$0")"
DIR="$(pwd)"

echo "Installing Python packages if needed..."
pip3 install -r requirements.txt
echo ""

echo "Configuring ngrok authtoken..."
ngrok config add-authtoken 3AvwkQkkLkHMSbwOITQbqnRtdcY_PrEEhBKZELM7qeVW2osC
echo ""

echo "-------------------------------------"
echo "Starting Flask server..."
echo "-------------------------------------"
osascript -e "tell app \"Terminal\" to do script \"cd '$DIR' && python3 app.py\""

echo "Waiting for Flask to boot..."
sleep 5

echo "-------------------------------------"
echo "Starting ngrok tunnel..."
echo "-------------------------------------"
osascript -e "tell app \"Terminal\" to do script \"cd '$DIR' && ngrok http 5000\""

echo ""
echo "====================================="
echo "Two windows should now be open:"
echo "1) Flask server"
echo "2) ngrok tunnel"
echo ""
echo "In the ngrok window look for:"
echo "Forwarding https://xxxxx.ngrok-free.app"
echo "====================================="
