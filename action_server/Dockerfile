FROM rasa/rasa-sdk:3.6.2

WORKDIR /app

COPY . .

# Install any extra Python dependencies (only if needed)
RUN pip install pymongo requests

# Default CMD (automatically starts action server):
# This is already the default CMD of rasa-sdk image, 
# but you can explicitly define it to avoid confusion
CMD ["start", "--actions", "actions", "--port", "5055", "--cors", "*", "--debug"]
