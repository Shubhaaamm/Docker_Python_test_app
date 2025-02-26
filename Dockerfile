# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask app port
EXPOSE 5000

# Run the Flask application
CMD [ "python", "app.py"]