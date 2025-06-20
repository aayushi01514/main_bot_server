FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . /app

CMD ["run", "--enable-api", "--cors", "*", "--debug", "--port", "8000"]
