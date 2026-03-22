# 04 — Troubleshooting

A log of every issue encountered setting up bloomburrow.sg, and exactly how each was fixed.

---

## Issue 1 — Domain Stuck on "Pending" in Cloudflare

**Symptom:** Cloudflare dashboard shows the domain as "Pending" for hours.

**Cause:** Exabytes nameservers had not been updated to point to Cloudflare.

**Fix:** Log in to Exabytes → Domain Management → Nameservers → replace default nameservers with the two Cloudflare nameservers shown in the Cloudflare dashboard. Propagation takes up to 24 hours. Status changes to Active once complete.

---

## Issue 2 — ERR_SSL_VERSION_OR_CIPHER_MISMATCH

**Symptom:** Browser shows this error when visiting https://bloomburrow.sg.

**Cause:** Cloudflare's Universal SSL certificate had not yet been issued.

**Fix:** Wait ~15 minutes after the domain becomes Active. Also ensure SSL/TLS mode in Cloudflare is set to **Full** (not Flexible). Check under SSL/TLS → Edge Certificates — the certificate will appear once issued.

---

## Issue 3 — Blank White Page

**Symptom:** https://bloomburrow.sg loads but shows a completely blank white page.

**Cause (first occurrence):** SSL was not yet fully active — the page was loading over HTTP, which the browser silently upgraded and then failed.

**Fix:** Waited for certificate to be issued. Also cleared browser cache and tested in Incognito mode to bypass cached errors.

---

## Issue 4 — HTTP ERROR 503

**Symptom:** Site returns 503 Service Unavailable.

**This has multiple root causes — check them in order:**

### 4a — Flask/Waitress not running
Check the Waitress CMD window. If it's closed or shows an error, re-run `run.bat`.

### 4b — Cloudflare Tunnel not running
Check the Cloudflare Tunnel CMD window. If it's closed, re-run `run.bat`. Confirm 4 connection lines are registered in the log.

### 4c — `localhost` resolving to IPv6 (main root cause)
**Symptom in tunnel log:** `originService=http://localhost:5000`

Waitress listens on `127.0.0.1` (IPv4 only) but `localhost` on Windows resolves to `::1` (IPv6). The tunnel cannot reach Waitress, causing every request to 503.

**Fix:** Edit `C:\Users\<YourName>\.cloudflared\config.yml` — change:
```yaml
service: http://localhost:5000
```
to:
```yaml
service: http://127.0.0.1:5000
```
`run.bat` now patches this automatically on every launch.

### 4d — Multiple cloudflared replicas (load balancing across dead instances)
**Symptom:** Cloudflare dashboard shows 2 or 3 replicas instead of 1. ~50% of requests hit a dead instance and 503.

**Cause:** `run.bat` was launched multiple times, or cloudflared was running as a Windows service in the background.

**Fix:**
1. Task Manager → Details → kill all `cloudflared.exe`
2. Close all CMD windows
3. Re-run `run.bat` once

`run.bat` now kills all cloudflared processes before starting a new one.

### 4e — Waitress queue full due to video streaming
**Symptom in Waitress log:** `WARNING:waitress.queue:Task queue depth is 1` appearing repeatedly, followed by disconnects.

**Cause:** The 3 autoplay videos on the homepage each hold a Waitress thread for the duration of the stream. With the default 4 threads, all threads fill up and new requests 503.

**Fix:** Increased Waitress thread count to 8 in `run.bat`:
```
waitress-serve --host=127.0.0.1 --port=5000 --threads=8 app:app
```
Also added a custom Flask route for video files with HTTP Range Request support, so browsers can stream chunks rather than downloading the whole file.

---

## Issue 5 — Both CMD Windows Close Immediately

**Symptom:** Running `run.bat` opens two CMD windows that instantly close.

**Cause:** The `cd` command in the batch file failed because the path `C:\Users\Aw Jia Yu\` contains a space, causing the rest of the command to be misinterpreted.

**Fix:** Changed from `cd "%~dp0"` to `cd /d "%~dp0"` and also added `/D "%~dp0"` to the `start` command so each subprocess also starts in the correct working directory:
```bat
start "Flask - Bloom Burrow" /D "%~dp0" cmd /k "waitress-serve ..."
```

---

## Issue 6 — Videos Not Loading / Client Disconnected Errors

**Symptom in Waitress log:**
```
INFO:waitress:Client disconnected while serving /static/videos/r6.mp4
```

**Cause:** Browsers stream video using HTTP Range Requests (requesting small chunks at a time). Flask's default static file serving doesn't handle range requests properly through Waitress, causing the browser to disconnect.

**Fix:** Added a custom Flask route in `app.py` that reads the `Range` header and returns a proper `206 Partial Content` response with exactly the bytes requested.

> **Note:** The "client disconnected" message still appears in logs even after this fix. This is **normal** — it means the browser buffered enough video and paused the download. Error code 0 in the tunnel log (`stream canceled by remote with error code 0`) also means the browser cleanly closed the connection. Neither is an actual error.

---

## Issue 7 — cloudflared Auto-Starting on Boot

**Symptom:** cloudflared.exe appears in Task Manager even before `run.bat` is launched, causing duplicate replicas.

**Cause:** cloudflared was installed as a Windows service at some point.

**Fix:** Open CMD as Administrator and run:
```cmd
cloudflared service uninstall
sc stop cloudflared
```

After this, cloudflared only runs when explicitly started by `run.bat`.

---

## Issue 8 — Cloudflare Rocket Loader Breaking Videos / JS

**Symptom:** Videos not autoplaying or JavaScript errors on the page.

**Cause:** Cloudflare's Rocket Loader feature rewrites and defers JS loading, which interferes with video autoplay attributes and some inline scripts.

**Fix:** Cloudflare Dashboard → bloomburrow.sg → Speed → Optimization → Rocket Loader → **Off**.

---

## Useful Diagnostic Commands

Check if Waitress is listening:
```cmd
netstat -an | findstr :5000
```
Should show: `TCP 127.0.0.1:5000 LISTENING`

Check if cloudflared is running:
```cmd
tasklist | findstr cloudflared
```

Test local site directly (bypassing the tunnel):
```
http://127.0.0.1:5000
```
If this works but bloomburrow.sg doesn't, the issue is in the tunnel or Cloudflare, not Flask.

Check tunnel logs for origin service URL:
Look for `originService=` in the Cloudflare Tunnel CMD window. It must show `http://127.0.0.1:5000`, not `http://localhost:5000`.
