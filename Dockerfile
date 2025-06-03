# Python image
FROM python:3.10.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port 5000 inside container (informational)
EXPOSE 5000

# Create unprivileged user and switch
RUN useradd -m appuser
USER appuser

# Use shell form for CMD so $PORT is expanded properly on Heroku
CMD ["sh", "-c", "gunicorn --workers=3 --bind=0.0.0.0:$PORT app:app"]
