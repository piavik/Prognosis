# Use the official Python image as the base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    DOCKER_MODEL_PATH=/app/models/

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ /app/app/

# Copy the models into the container
COPY models/ ${DOCKER_MODEL_PATH}

# Expose the port that the app will run on
EXPOSE 8089

# Command to run the application
CMD ["streamlit", "run", "app/main.py", "--server.port", "8089"]