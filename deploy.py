#!/usr/bin/env python3
"""
Deployment script for RealtyPro Real Estate Project
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def create_directories():
    """Create necessary directories"""
    directories = ['logs', 'media', 'staticfiles']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"📁 Created directory: {directory}")

def collect_static():
    """Collect static files"""
    return run_command(
        "python manage.py collectstatic --noinput",
        "Collecting static files"
    )

def run_migrations():
    """Run database migrations"""
    return run_command(
        "python manage.py migrate",
        "Running database migrations"
    )

def create_superuser():
    """Create superuser if needed"""
    print("👤 Do you want to create a superuser? (y/n): ", end="")
    response = input().lower().strip()
    if response == 'y':
        run_command(
            "python manage.py createsuperuser",
            "Creating superuser"
        )

def start_gunicorn():
    """Start Gunicorn server"""
    print("🚀 Starting Gunicorn server...")
    print("📝 Use Ctrl+C to stop the server")
    print("🌐 Server will be available at: http://localhost:8000")
    print("-" * 50)
    
    try:
        subprocess.run([
            "gunicorn",
            "--config", "gunicorn.conf.py",
            "realestate_project.wsgi:application"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Failed to start server: {e}")

def main():
    """Main deployment function"""
    print("🏠 RealtyPro Real Estate Project - Deployment Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("manage.py").exists():
        print("❌ Error: manage.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Run migrations
    if not run_migrations():
        print("❌ Migration failed. Please check your database configuration.")
        sys.exit(1)
    
    # Collect static files
    if not collect_static():
        print("❌ Static file collection failed.")
        sys.exit(1)
    
    # Create superuser
    create_superuser()
    
    # Start server
    start_gunicorn()

if __name__ == "__main__":
    main()
