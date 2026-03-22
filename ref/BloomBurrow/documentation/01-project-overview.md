# 01 — Project Overview

## What is Bloom Burrow?

Bloom Burrow (bloomburrow.sg) is a DIY wedding flower bar booking web app. Customers visit the site, browse packages, and submit a booking request. The admin (you) reviews bookings, confirms them, and tracks costs and profit through an admin dashboard.

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Web framework | Flask 3.0.3 | Handles all routes, forms, and logic |
| Database | SQLite via Flask-SQLAlchemy | Stores bookings, users |
| Authentication | Flask-Login | Admin login session management |
| Email | Flask-Mail (Gmail SMTP) | Booking confirmation emails |
| WSGI server | Waitress | Serves Flask in production (replaces Flask dev server) |
| Public access | Cloudflare Tunnel (cloudflared) | Exposes local server to the internet |
| Domain | bloomburrow.sg via Exabytes | Registered domain pointed to Cloudflare |
| DNS / CDN / SSL | Cloudflare | Nameservers, HTTPS certificate, DDoS protection |

---

## Folder Structure

```
BloomBurrow/
├── app.py                  # Main Flask application
├── run.bat                 # Launcher — starts Waitress + Cloudflare Tunnel
├── requirements.txt        # Python dependencies
│
├── templates/              # HTML pages (Jinja2)
│   ├── index.html          # Home page (hero, packages, gallery, What To Expect)
│   ├── book.html           # Booking request form
│   ├── booking_success.html
│   ├── chat.html           # Customer chat / booking view
│   ├── dashboard.html      # Customer: my bookings
│   └── admin/
│       └── dashboard.html  # Admin panel (orders, financials)
│
├── static/
│   ├── css/
│   │   └── style.css       # All site styles
│   ├── images/             # r1.jpg–r4.jpg (hero + gallery photos)
│   ├── videos/             # r6.mp4, r7.mp4, r8.mp4 (gallery videos)
│   └── uploads/            # Customer-uploaded inspiration photos
│
├── instance/
│   └── bloomburrow.db      # SQLite database (auto-created)
│
└── documentation/          # This folder
```

---

## Key Features

**Customer side:**
- Browse packages on the home page
- Submit a booking request with name, email, phone (+65), venue, pax, date, notes, and an inspiration photo upload
- View booking status and chat with admin on the customer dashboard
- Booking reference shown as e.g. `Booking #BB-1234 — 120 Pax Package`

**Admin side:**
- Login-protected admin dashboard
- Card layout showing all bookings with full details
- Confirm or reject bookings, reply to customer messages
- Input cost and hours spent per booking
- Financial summary at the top: total Cost, Profit, and Profit/Hour

---

## Python Dependencies

```
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-Mail==0.10.0
Werkzeug==3.0.3
waitress
```

Install with: `pip install -r requirements.txt`
