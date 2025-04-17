from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (hostname = redis, port = 6379)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    # Get current visit count (default to 0)
    count = r.get('visits')
    if count is None:
        count = 0
    else:
        count = int(count)

    # Increment and store it back
    count += 1
    r.set('visits', count)

    return f"Hello! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

