FROM rasa/rasa-sdk:3.6.2

USER root

# Install system dependencies required for pymongo
RUN apt-get update && apt-get install -y gcc python3-dev libffi-dev libssl-dev

WORKDIR /app

COPY . .

# Install your required Python dependencies
RUN pip install pymongo

CMD ["start", "--actions", "actions", "--port", "5055", "--cors", "*", "--debug"]
