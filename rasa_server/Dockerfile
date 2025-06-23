FROM rasa/rasa:3.6.21-full

USER root

WORKDIR /app

COPY . .

RUN chmod +x start.sh

USER 1001

EXPOSE 5005

CMD ["./start.sh"]
