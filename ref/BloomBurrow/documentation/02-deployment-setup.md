# 02 — Deployment Setup

This document explains how bloomburrow.sg was set up to serve a Flask app running on a personal Windows PC — no cloud server required.

---

## Architecture Overview

```
Visitor's Browser
       │  HTTPS
       ▼
  Cloudflare Edge (Singapore)
  • SSL certificate (Universal SSL)
  • DDoS protection
  • DNS resolution for bloomburrow.sg
       │  Cloudflare Tunnel (encrypted)
       ▼
  cloudflared.exe  (running on your PC)
       │  http://127.0.0.1:5000
       ▼
  Waitress WSGI server  (running on your PC)
       │
       ▼
  Flask app (app.py)
```

Traffic never touches a cloud server. Cloudflare's edge nodes connect back to your PC through the tunnel, so your home IP is never exposed.

---

## Step 1 — Domain Registration

- Domain **bloomburrow.sg** was registered with **Exabytes**
- `.sg` domains require a Singapore business/individual registration

---

## Step 2 — Add Domain to Cloudflare

1. Create a free account at https://cloudflare.com
2. Click **Add a Site** → enter `bloomburrow.sg`
3. Choose the **Free plan**
4. Cloudflare scans existing DNS records (none in this case)
5. Cloudflare provides two nameserver addresses, e.g.:
   - `aria.ns.cloudflare.com`
   - `bob.ns.cloudflare.com`

---

## Step 3 — Point Nameservers to Cloudflare (Exabytes)

1. Log in to Exabytes control panel
2. Go to **Domain Management → Nameservers**
3. Replace the default Exabytes nameservers with the two Cloudflare nameservers
4. Save — propagation takes a few hours (up to 24h)
5. Confirm in Cloudflare dashboard: status changes from **Pending** to **Active**

> **Note:** DNSSEC should be OFF during this process. Cloudflare will prompt you to disable it if needed.

---

## Step 4 — SSL/TLS Settings

In Cloudflare dashboard → **SSL/TLS → Overview:**
- Set mode to **Full** (not Flexible, not Full Strict)
- Cloudflare issues a free **Universal SSL** certificate automatically
- Wait ~15 minutes for the certificate to appear under **Edge Certificates**

> If you see `ERR_SSL_VERSION_OR_CIPHER_MISMATCH`, the certificate hasn't been issued yet — just wait.

---

## Step 5 — Install Cloudflare Tunnel

On your Windows PC, open CMD and run:

```
winget install --id Cloudflare.cloudflared
```

Or download the installer from https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/

---

## Step 6 — Authenticate and Create the Tunnel

```cmd
cloudflared tunnel login
```
This opens a browser — log in to your Cloudflare account and authorise.

```cmd
cloudflared tunnel create bloomburrow
```
This creates a named tunnel called `bloomburrow` and saves credentials to:
`C:\Users\<YourName>\.cloudflared\<tunnel-id>.json`

---

## Step 7 — Route the Domain to the Tunnel

```cmd
cloudflared tunnel route dns bloomburrow bloomburrow.sg
```

This creates a CNAME DNS record in Cloudflare pointing `bloomburrow.sg` to the tunnel. You can verify it in Cloudflare DNS dashboard — it should show a CNAME to `<tunnel-id>.cfargotunnel.com` with the orange cloud (proxied) enabled.

---

## Step 8 — Configure the Tunnel (config.yml)

The tunnel config lives at:
`C:\Users\<YourName>\.cloudflared\config.yml`

It should contain:

```yaml
tunnel: <your-tunnel-id>
credentials-file: C:\Users\<YourName>\.cloudflared\<tunnel-id>.json
ingress:
  - hostname: bloomburrow.sg
    service: http://127.0.0.1:5000
  - service: http_status:404
```

> **Critical:** Use `127.0.0.1:5000` NOT `localhost:5000`. On Windows, `localhost` can resolve to `::1` (IPv6) but Waitress only listens on IPv4 — causing 503 errors.

---

## Step 9 — Install Waitress

Waitress is a production-grade WSGI server for Windows. The Flask built-in dev server is not suitable for production.

```cmd
pip install waitress
```

---

## Step 10 — run.bat (the launcher)

Everything is tied together in `run.bat`. Double-clicking this file:

1. Patches `config.yml` to ensure `127.0.0.1` is used
2. Kills any leftover cloudflared or Flask processes from previous runs
3. Starts Waitress on `127.0.0.1:5000` with 8 threads
4. Waits 5 seconds for Flask to be ready
5. Starts the Cloudflare Tunnel

```bat
waitress-serve --host=127.0.0.1 --port=5000 --threads=8 app:app
cloudflared tunnel run --url http://127.0.0.1:5000 bloomburrow
```

---

## Step 11 — Disable the cloudflared Windows Service

At some point cloudflared may have been installed as a Windows service, causing it to auto-start on boot and create duplicate tunnel replicas. To remove it:

Open CMD **as Administrator**:
```cmd
cloudflared service uninstall
sc stop cloudflared
```

After this, cloudflared only runs when you launch `run.bat`.

---

## Cloudflare Settings Summary

| Setting | Value |
|---------|-------|
| SSL/TLS mode | Full |
| DNS record type | CNAME (proxied / orange cloud) |
| Tunnel name | bloomburrow |
| Origin service | http://127.0.0.1:5000 |
| Rocket Loader | Disabled (causes JS issues with video autoplay) |
