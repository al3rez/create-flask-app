import os
from fabric import task, Connection
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get deployment settings from environment variables
HOST = os.getenv('HOST')
USER = os.getenv('USER')
APP_NAME = os.getenv('APP_NAME')
DOMAIN = os.getenv('DOMAIN')
REPO_URL = os.getenv('REPO_URL')
PROJECT_PATH = os.getenv('PROJECT_PATH')
VENV_PATH = os.getenv('VENV_PATH')
BRANCH = os.getenv('BRANCH', 'main')
GITHUB_DEPLOY_KEY = os.getenv('GITHUB_DEPLOY_KEY')
PORT = os.getenv('PORT', '8766')

@task
def setup(ctx):
    """Set up the server with Python, Nginx, and the application."""
    conn = Connection(host=HOST, user=USER)
    
    # Update system and install dependencies
    conn.sudo('apt-get update')
    conn.sudo('apt-get install -y python3-venv python3-pip nginx certbot python3-certbot-nginx')
    
    # Create project directory
    conn.sudo(f'mkdir -p {PROJECT_PATH}')
    conn.sudo(f'chown {USER}:{USER} {PROJECT_PATH}')
    
    # Clone repository
    with conn.cd(PROJECT_PATH):
        conn.run(f'git clone {REPO_URL} .')
        conn.run(f'git checkout {BRANCH}')
    
    # Set up virtual environment
    with conn.cd(PROJECT_PATH):
        conn.run(f'python3 -m venv {VENV_PATH}')
        with conn.prefix(f'source {VENV_PATH}/bin/activate'):
            conn.run('pip install -r requirements.txt')
    
    # Set up Nginx
    nginx_config = f'{PROJECT_PATH}/templates/nginx_config.j2'
    conn.sudo(f'envsubst < {nginx_config} > /etc/nginx/sites-available/{APP_NAME}')
    conn.sudo(f'ln -sf /etc/nginx/sites-available/{APP_NAME} /etc/nginx/sites-enabled/')
    conn.sudo('nginx -t')
    conn.sudo('systemctl reload nginx')
    
    # Set up SSL with Certbot
    conn.sudo(f'certbot --nginx -d {DOMAIN} --non-interactive --agree-tos --email your-email@example.com')
    
    # Set up systemd service
    service_config = f'{PROJECT_PATH}/templates/systemd_service.j2'
    conn.sudo(f'envsubst < {service_config} > /etc/systemd/system/{APP_NAME}.service')
    conn.sudo('systemctl daemon-reload')
    conn.sudo(f'systemctl enable {APP_NAME}')
    conn.sudo(f'systemctl start {APP_NAME}')

@task
def deploy(ctx):
    """Deploy latest changes to the server."""
    conn = Connection(host=HOST, user=USER)
    
    with conn.cd(PROJECT_PATH):
        # Pull latest changes
        conn.run(f'git pull origin {BRANCH}')
        
        # Update dependencies
        with conn.prefix(f'source {VENV_PATH}/bin/activate'):
            conn.run('pip install -r requirements.txt')
        
        # Restart service
        conn.sudo(f'systemctl restart {APP_NAME}')

@task
def logs(ctx):
    """View application logs."""
    conn = Connection(host=HOST, user=USER)
    conn.sudo(f'journalctl -u {APP_NAME} -f') 