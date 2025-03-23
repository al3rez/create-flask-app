from flask_cors import CORS

def add_cors(app):
    CORS(app, resources={r"/*": {"origins": "*"}})  # Adjust origins as needed 