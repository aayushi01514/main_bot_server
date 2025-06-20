FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc

RUN pip install rasa-sdk==3.6.2 pymongo requests

WORKDIR /app

COPY . .

EXPOSE 5055

CMD ["rasa", "run", "actions", "--port", "5055", "--cors", "*", "--debug"]
