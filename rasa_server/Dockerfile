FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD /bin/sh -c "rasa run --enable-api --cors '*' --debug --port ${PORT}"
