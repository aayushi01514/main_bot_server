FROM rasa/rasa-sdk:3.6.2

WORKDIR /app

COPY . .

# Install any extra packages your actions.py needs:
RUN pip install pymongo requests

# The rasa-sdk image automatically runs:
# start --actions actions
# so you don't need to define CMD again unless you customize it
