# Flask API Project

This is a Flask-based API project generated using create-flask-app.

## Setup

1. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On Unix/macOS
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

## Development

Run the development server:
```bash
python app/main.py
```

The API will be available at http://localhost:8766

## Deployment

This project includes Fabric deployment scripts and templates for Nginx and systemd.

1. Configure your server details in `.env`

2. Deploy using Fabric:
   ```bash
   fab setup
   ```

## API Endpoints

- `GET /health`: Health check endpoint
- `GET /`: Welcome message

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── cors.py      # CORS configuration
│   ├── db.py        # Database configuration
│   └── main.py      # Main application
├── templates/       # Deployment templates
│   ├── nginx_config.j2
│   └── systemd_service.j2
├── .env.example
├── .gitignore
├── fabfile.py
├── README.md
└── requirements.txt
``` 