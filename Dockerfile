# Use Python image
FROM python:3.10.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask numpy scikit-learn joblib

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
