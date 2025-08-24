#!/bin/bash
# Render Deployment Script for RealtyPro Real Estate Project

echo "🚀 Starting Render deployment..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if needed (optional)
# echo "👤 Creating superuser..."
# python manage.py createsuperuser --noinput

echo "✅ Deployment setup completed!"
echo "🌐 Starting Gunicorn server..."

# Start Gunicorn
exec gunicorn realestate_project.wsgi:application
