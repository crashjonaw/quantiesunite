#!/bin/bash
# Run Playwright tests (assumes app is running on localhost:5001)
cd "$(dirname "$0")"
pytest . -v "$@"
