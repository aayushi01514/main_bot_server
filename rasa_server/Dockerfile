# Use the official Rasa image
FROM rasa/rasa:3.6.21

# Set working directory
WORKDIR /app

# Copy all project files to container
COPY . /app

# Install any additional dependencies if needed
# Uncomment if you have a requirements.txt for additional dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Expose Rasa server port
EXPOSE 5005

# Start Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
