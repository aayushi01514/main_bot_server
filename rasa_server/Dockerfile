FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . /app

EXPOSE 5005

CMD bash -c "rasa run --enable-api --cors '*' --debug --port ${PORT:-5005}"