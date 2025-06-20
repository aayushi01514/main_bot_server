FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD rasa run --enable-api --cors "*" --debug --port ${PORT}
