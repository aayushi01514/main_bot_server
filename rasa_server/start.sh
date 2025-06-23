#!/bin/sh

# Default to 5005 for local dev
PORT=${PORT:-5005}

echo "Starting Rasa server on port ${PORT}"

rasa run --enable-api --cors "*" --debug --port ${PORT}
