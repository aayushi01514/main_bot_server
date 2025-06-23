#!/bin/sh

# Default fallback port if PORT not provided
PORT=${PORT:-5005}

echo "Starting Rasa Server on port ${PORT}"

rasa run --enable-api --cors "*" --debug --port ${PORT}
