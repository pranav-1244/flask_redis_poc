# Flask + Redis Docker POC

This is a proof of concept (POC) that demonstrates how to run a **Flask web app** and a **Redis database** in Docker containers using **Docker Compose**.

## Features
- **Flask** web app that displays how many times the page has been visited.
- **Redis** used as a simple in-memory database to keep track of visit count.
- **Docker Compose** used to run Flask and Redis containers together.

## Prerequisites
- Docker and Docker Compose installed.

## Project Structure
flask_redis_poc/ ├── app.py # Flask application code ├── requirements.txt # Python dependencies ├── Dockerfile # Dockerfile for Flask app └── docker-compose.yml # Docker Compose configuration

bash
Copy
Edit

## Steps to Run the POC

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd flask_redis_poc
Build and run the containers using Docker Compose:

bash
Copy
Edit
docker-compose up --build
The --build flag rebuilds the Flask app image, ensuring you have the latest changes.

Access the app:

Open your browser and visit http://localhost:5000. The page will show how many times it’s been visited.

Stop the services:

To stop and remove the containers, use:

bash
Copy
Edit
docker-compose down
How It Works
Flask is a Python web framework that runs a simple app.

Redis is an in-memory key-value store used here to count the number of visits.

Docker Compose orchestrates the running of both services (Flask + Redis) in separate containers.
