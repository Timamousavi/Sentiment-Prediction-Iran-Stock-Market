# Iranian Stock Market Sentiment Analysis - Deployment Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Deployment](#local-deployment)
3. [Production Deployment](#production-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Cloud Deployment](#cloud-deployment)
6. [Monitoring and Logging](#monitoring-and-logging)
7. [Scaling](#scaling)
8. [Maintenance](#maintenance)

## Prerequisites

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum
- 2 CPU cores minimum
- 10GB disk space

### Software Requirements
- Git
- Docker (optional)
- Nginx (for production)
- Supervisor (for process management)

### Environment Variables
Create a `.env` file with:
```
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# Security
SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database (if using)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sentiment_db
DB_USER=user
DB_PASSWORD=password

# Logging
LOG_LEVEL=INFO
LOG_FILE=app.log

# Model Configuration
MODEL_PATH=models/v1
```

## Local Deployment

### 1. Clone Repository
```bash
git clone https://github.com/your-repo/iranian-stock-sentiment-analysis.git
cd iranian-stock-sentiment-analysis
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

## Production Deployment

### 1. System Setup
```bash
# Update system
sudo apt update
sudo apt upgrade

# Install required packages
sudo apt install python3-pip python3-venv nginx supervisor
```

### 2. Application Setup
```bash
# Create application directory
sudo mkdir /opt/sentiment-analysis
sudo chown $USER:$USER /opt/sentiment-analysis

# Clone repository
cd /opt/sentiment-analysis
git clone https://github.com/your-repo/iranian-stock-sentiment-analysis.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Nginx Configuration
Create `/etc/nginx/sites-available/sentiment-analysis`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/sentiment-analysis /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 4. Supervisor Configuration
Create `/etc/supervisor/conf.d/sentiment-analysis.conf`:
```ini
[program:sentiment-analysis]
command=/opt/sentiment-analysis/venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8000
directory=/opt/sentiment-analysis
user=your-user
autostart=true
autorestart=true
stderr_logfile=/var/log/sentiment-analysis.err.log
stdout_logfile=/var/log/sentiment-analysis.out.log
```

Start service:
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start sentiment-analysis
```

## Docker Deployment

### 1. Build Image
```bash
docker build -t sentiment-analysis .
```

### 2. Run Container
```bash
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/logs:/app/logs \
  --env-file .env \
  sentiment-analysis
```

### 3. Docker Compose
Create `docker-compose.yml`:
```yaml
version: '3'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./models:/app/models
      - ./logs:/app/logs
    env_file:
      - .env
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## Cloud Deployment

### AWS Deployment
1. Create EC2 instance
2. Install Docker
3. Deploy using Docker Compose
4. Set up Route 53 for DNS
5. Configure security groups

### Google Cloud Deployment
1. Create Compute Engine instance
2. Install Docker
3. Deploy using Docker Compose
4. Set up Cloud DNS
5. Configure firewall rules

### Azure Deployment
1. Create App Service
2. Configure deployment center
3. Set up custom domain
4. Configure SSL

## Monitoring and Logging

### Logging Configuration
```python
# In src/api/main.py
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Monitoring Setup
1. Install Prometheus
2. Configure Grafana
3. Set up alerts

Example Prometheus config:
```yaml
scrape_configs:
  - job_name: 'sentiment-analysis'
    static_configs:
      - targets: ['localhost:8000']
```

## Scaling

### Horizontal Scaling
1. Set up load balancer
2. Configure multiple instances
3. Use shared storage for models

### Vertical Scaling
1. Increase instance size
2. Optimize model loading
3. Implement caching

## Maintenance

### Regular Tasks
1. Update dependencies
2. Backup models and data
3. Monitor performance
4. Check logs

### Backup Strategy
```bash
# Backup models
tar -czf models_backup.tar.gz models/

# Backup logs
tar -czf logs_backup.tar.gz logs/
```

### Update Procedure
1. Pull latest changes
2. Run tests
3. Backup current version
4. Deploy new version
5. Verify functionality

## Troubleshooting

### Common Issues
1. **Model Loading Error**
   - Check model path
   - Verify permissions
   - Check disk space

2. **Performance Issues**
   - Monitor resource usage
   - Check logs
   - Optimize configuration

3. **API Errors**
   - Check error logs
   - Verify configuration
   - Test endpoints

### Debugging
```bash
# Check logs
tail -f app.log

# Check process status
supervisorctl status

# Check nginx logs
tail -f /var/log/nginx/error.log
```

## Security

### SSL Configuration
```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Security Best Practices
1. Use HTTPS
2. Implement rate limiting
3. Regular security updates
4. Monitor access logs
5. Use strong passwords 