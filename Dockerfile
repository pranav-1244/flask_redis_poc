# Use a small Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file and install packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire app code
COPY . .

# Run the app
CMD ["python", "app.py"]
