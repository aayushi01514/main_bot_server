FROM rasa/rasa-sdk:3.6.2

WORKDIR /app

# Add system packages required for pip to build some dependencies
USER root

RUN apt-get update && apt-get install -y gcc python3-dev libffi-dev libssl-dev

COPY . .

# Install your extra Python dependencies after system dependencies
RUN pip install pymongo requests

CMD ["start", "--actions", "actions", "--port", "5055", "--cors", "*", "--debug"]
