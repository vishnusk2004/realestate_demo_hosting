"""
Gunicorn configuration file for RealtyPro Real Estate Project
"""
import multiprocessing
import os

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2

# Restart workers after this many requests, to help prevent memory leaks
preload_app = True

# Logging
accesslog = "logs/gunicorn_access.log"
errorlog = "logs/gunicorn_error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = "realtypro"

# Server mechanics
daemon = False
pidfile = "logs/gunicorn.pid"
user = None
group = None
tmp_upload_dir = None

# SSL (uncomment when you have SSL certificates)
# keyfile = "path/to/keyfile"
# certfile = "path/to/certfile"

# Server hooks
def on_starting(server):
    """Log when server starts"""
    server.log.info("Starting RealtyPro Gunicorn server")

def on_reload(server):
    """Log when server reloads"""
    server.log.info("Reloading RealtyPro Gunicorn server")

def worker_int(worker):
    """Log when worker receives SIGINT"""
    worker.log.info("Worker received SIGINT")

def pre_fork(server, worker):
    """Log before forking worker"""
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def post_fork(server, worker):
    """Log after forking worker"""
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def post_worker_init(worker):
    """Log after worker initialization"""
    worker.log.info("Worker initialized (pid: %s)", worker.pid)

def worker_abort(worker):
    """Log when worker aborts"""
    worker.log.info("Worker aborted (pid: %s)", worker.pid)

def pre_exec(server):
    """Log before exec"""
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    """Log when server is ready"""
    server.log.info("Server is ready. Spawning workers")

def worker_exit(server, worker):
    """Log when worker exits"""
    server.log.info("Worker exited (pid: %s)", worker.pid)

def on_exit(server):
    """Log when server exits"""
    server.log.info("Server exiting")
