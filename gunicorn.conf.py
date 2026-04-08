"""
Gunicorn configuration for QuantiesUnite.

Run with:  gunicorn -c gunicorn.conf.py app:app
Or just:   gunicorn app:app  (uses this file automatically if in the same dir)

Tuned for ~1000 concurrent users on a modest VPS (2-4 CPU cores, 2-4 GB RAM).
"""

import multiprocessing
import os

# ── Bind ──────────────────────────────────────────────────────────────────────
bind = os.environ.get("GUNICORN_BIND", "127.0.0.1:5001")

# ── Workers ───────────────────────────────────────────────────────────────────
# Rule of thumb: (2 × CPU cores) + 1
# Each worker is an independent process with its own memory.
# Override with GUNICORN_WORKERS env var for different machines.
workers = int(os.environ.get("GUNICORN_WORKERS", min(multiprocessing.cpu_count() + 1, 4)))

# ── Threads per worker ────────────────────────────────────────────────────────
# Each worker spawns this many threads. Total concurrency = workers × threads.
# For a 4-core machine: 9 workers × 4 threads = 36 concurrent requests.
# That's plenty for 1000 users (most are idle/reading at any moment).
threads = int(os.environ.get("GUNICORN_THREADS", 4))

# ── Worker class ──────────────────────────────────────────────────────────────
# gthread = threaded workers (best for I/O-bound Flask apps with SQLite)
worker_class = "gthread"

# ── Timeouts ──────────────────────────────────────────────────────────────────
timeout = 120          # Kill worker if a request takes > 120s
graceful_timeout = 30  # Allow 30s for in-flight requests on restart
keepalive = 5          # Keep connections alive for 5s between requests

# ── Max requests (memory leak protection) ─────────────────────────────────────
max_requests = 1000        # Restart worker after 1000 requests
max_requests_jitter = 100  # Add random jitter to avoid all workers restarting at once

# ── Preload ───────────────────────────────────────────────────────────────────
# Load the app before forking workers — saves memory via copy-on-write
# and catches import errors early.
preload_app = False

# ── Logging ───────────────────────────────────────────────────────────────────
accesslog = "-"                    # Log to stdout (captured by systemd/supervisor)
errorlog = "-"
loglevel = os.environ.get("GUNICORN_LOGLEVEL", "info")
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" %(D)sμs'

# ── Process naming ────────────────────────────────────────────────────────────
proc_name = "quantiesunite"

# ── Lifecycle hooks ───────────────────────────────────────────────────────────
def on_starting(server):
    print("=" * 55)
    print("  QuantiesUnite — Gunicorn")
    print(f"  Bind:    {bind}")
    print(f"  Workers: {workers} × {threads} threads = {workers * threads} concurrent")
    print("  Press Ctrl+C to stop")
    print("=" * 55)
