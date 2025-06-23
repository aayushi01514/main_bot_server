FROM rasa/rasa:3.6.21

WORKDIR /app

COPY . /app

# If you have extra Python packages:
# RUN pip install -r requirements.txt

EXPOSE 5005

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug", "--endpoints", "endpoints.yml"]
