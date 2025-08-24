# 🚀 RealtyPro Real Estate Project - Deployment Guide

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd reachrajforreal_realestate_web_dev
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the project root:
```bash
# Django Settings
SECRET_KEY=your-super-secret-key-change-this-in-production
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database Settings
DATABASE_URL=sqlite:///db.sqlite3

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security Settings
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

## 🚀 Quick Deployment

### Option 1: Using the Deployment Script
```bash
python deploy.py
```

### Option 2: Manual Deployment

#### 1. Run Migrations
```bash
python manage.py migrate
```

#### 2. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

#### 3. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

#### 4. Start Gunicorn Server
```bash
gunicorn --config gunicorn.conf.py realestate_project.wsgi:application
```

## 🌐 Production Deployment

### Using Gunicorn
```bash
# Basic Gunicorn command
gunicorn realestate_project.wsgi:application

# With custom configuration
gunicorn --config gunicorn.conf.py realestate_project.wsgi:application

# With specific settings
gunicorn --bind 0.0.0.0:8000 --workers 4 realestate_project.wsgi:application
```

### Using Production Settings
```bash
# Set Django settings to production
export DJANGO_SETTINGS_MODULE=realestate_project.production

# Run with production settings
gunicorn --config gunicorn.conf.py realestate_project.wsgi:application
```

## 🔧 Configuration Files

### Gunicorn Configuration (`gunicorn.conf.py`)
- **Workers**: Automatically calculated based on CPU cores
- **Port**: 8000 (configurable)
- **Logging**: Detailed access and error logs
- **Performance**: Optimized for production workloads

### Production Settings (`realestate_project/production.py`)
- **Security**: Enhanced security headers
- **Logging**: Comprehensive logging configuration
- **Static Files**: WhiteNoise integration
- **Performance**: Database and cache optimizations

## 📊 Monitoring & Logs

### Log Files Location
- **Django Logs**: `logs/django.log`
- **Gunicorn Access Logs**: `logs/gunicorn_access.log`
- **Gunicorn Error Logs**: `logs/gunicorn_error.log`

### View Logs
```bash
# View Django logs
tail -f logs/django.log

# View Gunicorn access logs
tail -f logs/gunicorn_access.log

# View Gunicorn error logs
tail -f logs/gunicorn_error.log
```

## 🔒 Security Considerations

### 1. Environment Variables
- Never commit `.env` files to version control
- Use strong, unique SECRET_KEY
- Configure proper ALLOWED_HOSTS

### 2. HTTPS Setup
For production, enable HTTPS:
```python
# In production.py
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 3. Database Security
- Use strong database passwords
- Consider PostgreSQL for production
- Regular database backups

## 🚀 Deployment Platforms

### Heroku
```bash
# Create Procfile
echo "web: gunicorn realestate_project.wsgi:application" > Procfile

# Deploy
git push heroku main
```

### DigitalOcean App Platform
- Connect your Git repository
- Set build command: `pip install -r requirements.txt`
- Set run command: `gunicorn realestate_project.wsgi:application`

### AWS/GCP/Azure
- Use their respective deployment services
- Configure environment variables
- Set up load balancers for multiple instances

## 🔧 Troubleshooting

### Common Issues

#### 1. Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT in settings
```

#### 2. Database Migration Errors
```bash
# Reset migrations (if needed)
python manage.py migrate --fake-initial

# Check database connection
python manage.py dbshell
```

#### 3. Gunicorn Not Starting
```bash
# Check if port is in use
netstat -tulpn | grep :8000

# Check Gunicorn logs
tail -f logs/gunicorn_error.log
```

#### 4. Permission Issues
```bash
# Fix directory permissions
chmod 755 logs/
chmod 755 media/
chmod 755 staticfiles/
```

## 📈 Performance Optimization

### 1. Database Optimization
- Use database indexes
- Optimize queries
- Consider database connection pooling

### 2. Caching
- Enable Django caching
- Use Redis for session storage
- Implement CDN for static files

### 3. Gunicorn Tuning
- Adjust worker count based on CPU cores
- Monitor memory usage
- Set appropriate timeout values

## 🆘 Support

For deployment issues:
1. Check the logs in `logs/` directory
2. Verify environment variables
3. Ensure all dependencies are installed
4. Check file permissions

## 📝 License

This project is licensed under the MIT License.
