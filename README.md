# Flask VPS Deployment Boilerplate

This is a powerful Flask API boilerplate that helps you deploy Flask applications to any VPS (Virtual Private Server) provider, avoiding vendor lock-in. Here are its key features:

## VPS Provider Independence
- Works with any VPS provider (DigitalOcean, Linode, Vultr, etc.)
- Typically much cheaper than serverless platforms like Vercel
- Full control over your infrastructure

## Automated Deployment
- Uses Fabric for automated deployments
- Sets up Nginx as reverse proxy
- Configures SSL certificates automatically using Let's Encrypt
- Sets up systemd service for process management

## Production-Ready Features
- CORS configuration
- Database integration support
- Nginx configured with:
  - HTTPS redirection
  - Gzip compression
  - Caching
  - HTTP/2 support

## Cost Comparison
- VPS costs typically start at $5/month (DigitalOcean, Linode)
- Much cheaper than serverless for consistent workloads
- No per-request pricing or cold starts

## Usage

```
pip install create-flask-vps-app
create-flask-vps-app myapp
cd myapp
fab setup
fab deploy
```

## When to Use
This boilerplate is particularly useful when you want to:
- Avoid vendor lock-in
- Keep costs predictable and low
- Have full control over your infrastructure
- Need better performance than serverless platforms
- Want automated deployment with best practices built-in