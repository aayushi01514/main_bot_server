FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . /app

EXPOSE 8000

# Use shell form directly (do not wrap inside /bin/sh -c again)
CMD rasa run --enable-api --cors "*" --debug --port $PORT
