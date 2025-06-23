FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . .

# Ensure start.sh is executable
RUN chmod +x start.sh

EXPOSE 5005

# Use shell form CMD (array form is not needed here)
CMD ["./start.sh"]
