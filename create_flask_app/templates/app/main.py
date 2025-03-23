from flask import Flask
from .cors import add_cors
from .db import init_db

app = Flask(__name__)

# Add CORS
add_cors(app)

# Initialize database (placeholder)
init_db()

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/')
def home():
    return {"message": "Welcome to the Flask API!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8766) 