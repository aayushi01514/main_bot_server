FROM rasa/rasa:3.6.21-full

WORKDIR /app

COPY . .

# Expose default Rasa port (for local clarity)
EXPOSE 5005

# Make start.sh executable
RUN chmod +x start.sh

# Use entrypoint script
CMD ["./start.sh"]
