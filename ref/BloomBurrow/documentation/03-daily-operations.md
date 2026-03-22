# 03 — Daily Operations

## Starting the Site

1. Navigate to the `BloomBurrow` folder
2. Double-click **`run.bat`**
3. Two CMD windows will open:
   - **"Flask - Bloom Burrow"** — the Waitress web server
   - **"Cloudflare Tunnel"** — the tunnel connecting your PC to bloomburrow.sg
4. Wait ~10 seconds for both to fully start
5. Visit https://bloomburrow.sg to confirm it's live

> The launcher window (the original bat window) will show a summary and then pause. You can minimise or close it — the two CMD windows are what keep the site running.

---

## Confirming the Site is Running

**Check the Flask/Waitress window** — you should see:
```
INFO:waitress:Serving on http://127.0.0.1:5000
```

**Check the Cloudflare Tunnel window** — you should see lines like:
```
INF Registered tunnel connection connIndex=0 ... location=sin21
INF Registered tunnel connection connIndex=1 ... location=sin22
INF Registered tunnel connection connIndex=2 ... location=sin08
INF Registered tunnel connection connIndex=3 ... location=sin09
```
Four connections registered = tunnel is healthy.

**Check Cloudflare Dashboard** → bloomburrow.sg → Zero Trust → Tunnels → bloomburrow → should show **Healthy** with **1 replica**.

---

## Stopping the Site

Simply close both CMD windows:
- "Flask - Bloom Burrow"
- "Cloudflare Tunnel"

The site will go offline once both are closed.

---

## Checking for Duplicate Tunnel Replicas

If the Cloudflare dashboard shows more than 1 replica, old cloudflared processes are still running. Fix:

1. Open **Task Manager** → **Details** tab
2. Kill every `cloudflared.exe` process
3. Close all open CMD windows from previous runs
4. Re-run `run.bat` once

Going forward `run.bat` automatically kills old processes before starting new ones.

---

## Accessing the Admin Panel

Visit: https://bloomburrow.sg/admin

Log in with your admin credentials. From here you can:
- View all booking requests
- Confirm or reject bookings
- Reply to customer messages
- Enter cost and hours spent per booking
- See total Profit and Profit/Hour at the top

---

## Checking Waitress Logs

The Waitress CMD window logs every request. Normal messages:

| Message | Meaning |
|---------|---------|
| `INFO:waitress:Serving on http://127.0.0.1:5000` | Server started successfully |
| `INFO:waitress:Client disconnected while serving /static/videos/r6.mp4` | Normal — browser buffered enough video and paused the download |
| `WARNING:waitress.queue:Task queue depth is 1` | Queue is filling — too many concurrent requests. If persistent, a 503 may follow |

---

## Database Location

The SQLite database is at:
```
BloomBurrow/instance/bloomburrow.db
```

This file contains all bookings and user accounts. Back it up regularly by copying it to a safe location.

---

## Adding a New Admin Account

In CMD from the BloomBurrow folder:
```cmd
python -c "from app import db, User; from werkzeug.security import generate_password_hash; u=User(email='you@email.com', password_hash=generate_password_hash('yourpassword'), is_admin=True); db.session.add(u); db.session.commit(); print('Done')"
```

---

## What Happens If Your PC Restarts

The site goes offline. You need to re-run `run.bat` manually to bring it back up. There is no auto-start configured (the cloudflared Windows service was intentionally removed to prevent duplicate replicas).

If you want the site to start automatically on boot, create a shortcut to `run.bat` in:
```
C:\Users\<YourName>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
