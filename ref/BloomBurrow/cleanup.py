"""
Bloom Burrow — One-Time Cleanup Script
---------------------------------------
Run this script while the Flask server is STOPPED to:
  - Delete all non-admin user accounts
  - Delete all bookings and chat messages
  - Reset the admin password to a new value
  - Clear accounts.csv and orders.csv

Usage:
    python cleanup.py
"""

import sqlite3
import hashlib
import secrets
import csv
import os

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DB_PATH      = os.path.join(BASE_DIR, 'instance', 'bloomburrow.db')
ACCOUNTS_CSV = os.path.join(BASE_DIR, 'accounts.csv')
ORDERS_CSV   = os.path.join(BASE_DIR, 'orders.csv')

# ── Set the new admin password here ──────────────────────────────────────────
ADMIN_PASSWORD = 'JYVS2026'
# ─────────────────────────────────────────────────────────────────────────────


def pbkdf2_hash(password):
    """Generate a werkzeug-compatible pbkdf2:sha256 hash."""
    salt = secrets.token_hex(16)
    dk   = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 260000, dklen=32)
    return f'pbkdf2:sha256:260000${salt}${dk.hex()}'


def run():
    if not os.path.isfile(DB_PATH):
        print(f"ERROR: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    # Delete all chat messages
    cur.execute('DELETE FROM chat_message')
    print(f"  Chat messages deleted.")

    # Delete all bookings
    cur.execute('DELETE FROM booking')
    print(f"  Bookings deleted.")

    # Delete all non-admin users
    cur.execute('DELETE FROM user WHERE is_admin = 0')
    print(f"  Non-admin users deleted.")

    # Update admin password
    new_hash = pbkdf2_hash(ADMIN_PASSWORD)
    cur.execute('UPDATE user SET password_hash = ? WHERE email = ?', (new_hash, 'admin'))
    print(f"  Admin password updated to '{ADMIN_PASSWORD}'.")

    conn.commit()

    # Verify
    cur.execute('SELECT id, name, email, is_admin FROM user')
    users = cur.fetchall()
    print(f"\n  Remaining users: {users}")
    cur.execute('SELECT COUNT(*) FROM booking')
    print(f"  Remaining bookings: {cur.fetchone()[0]}")
    conn.close()

    # Clear CSV files
    with open(ACCOUNTS_CSV, 'w', newline='', encoding='utf-8') as f:
        csv.DictWriter(f, fieldnames=['id', 'name', 'email', 'password', 'created_at']).writeheader()
    print(f"  accounts.csv cleared.")

    with open(ORDERS_CSV, 'w', newline='', encoding='utf-8') as f:
        csv.DictWriter(f, fieldnames=[
            'booking_id', 'user_id', 'user_name', 'user_email',
            'package', 'pax', 'price', 'event_date', 'event_venue',
            'notes', 'status', 'payment_status', 'created_at',
        ]).writeheader()
    print(f"  orders.csv cleared.")

    print("\nCleanup complete. You can now restart the server.")


if __name__ == '__main__':
    print("Bloom Burrow Cleanup Script")
    print("=" * 40)
    confirm = input("This will DELETE all user accounts, bookings, and messages. Continue? (yes/no): ")
    if confirm.strip().lower() == 'yes':
        run()
    else:
        print("Aborted.")
