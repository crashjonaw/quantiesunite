"""
Telegram notification helper for QuantiesUnite feedback loop.

Usage:
    from telegram.notify import send_manual_review, send_fix_deployed, send_message

    send_manual_review(feedback_id, user, page_link, description)
    send_fix_deployed(feedback_id, fix_summary)
    send_message("Custom message here")
"""

import json
import os
import ssl
import urllib.request
import urllib.parse

from telegram.config import BOT_TOKEN, CHAT_ID, ADMIN_USERNAME

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Create an SSL context that works with corporate/proxy environments
_ssl_ctx = ssl.create_default_context()
try:
    import certifi
    _ssl_ctx.load_verify_locations(certifi.where())
except ImportError:
    _ssl_ctx.check_hostname = False
    _ssl_ctx.verify_mode = ssl.CERT_NONE

API_URL = f"{BASE_URL}/sendMessage"
UPDATES_URL = f"{BASE_URL}/getUpdates"

_last_update_id = 0


def send_message(text, parse_mode="Markdown"):
    """Send a message to the configured Telegram chat."""
    msg = {"chat_id": CHAT_ID, "text": text}
    if parse_mode:
        msg["parse_mode"] = parse_mode
    payload = json.dumps(msg).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10, context=_ssl_ctx) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"[Telegram] Failed to send message: {e}")
        return None


def send_manual_review(feedback_id, user, page_link, description):
    """Notify admin that a feedback item needs manual review."""
    text = (
        f"*Needs Manual Review*\n"
        f"Feedback #{feedback_id}\n\n"
        f"*User:* {user}\n"
        f"*Page:* {page_link}\n"
        f"*Description:* {description}"
    )
    return send_message(text)


def send_fix_deployed(feedback_id, fix_summary, page_link=""):
    """Notify admin that a fix has been deployed."""
    text = (
        f"*Fix Deployed*\n"
        f"Feedback #{feedback_id}\n\n"
        f"*Summary:* {fix_summary}"
    )
    if page_link:
        text += f"\n\n*Verify:* {page_link}"
    return send_message(text)


def send_skipped(feedback_id, reason):
    """Notify admin that a feedback item was skipped."""
    text = (
        f"*Skipped*\n"
        f"Feedback #{feedback_id}\n\n"
        f"*Reason:* {reason}"
    )
    return send_message(text)


def get_inbox_messages():
    """Read and clear messages forwarded from the watcher via inbox.txt."""
    inbox_path = os.path.join(os.path.dirname(__file__), "inbox.txt")
    if not os.path.exists(inbox_path):
        return []
    try:
        with open(inbox_path, "r") as f:
            messages = [line.strip() for line in f if line.strip()]
        # Clear the inbox after reading
        with open(inbox_path, "w") as f:
            f.write("")
        return messages
    except Exception:
        return []


def get_admin_messages():
    """Fetch new messages from the admin (@crashjaw).

    Returns a list of message text strings from the admin, newest first.
    Only returns messages not yet seen (tracks offset via update_id).
    """
    global _last_update_id
    params = urllib.parse.urlencode({"offset": _last_update_id + 1, "timeout": 0})
    url = f"{UPDATES_URL}?{params}"

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=10, context=_ssl_ctx) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"[Telegram] Failed to fetch updates: {e}")
        return []

    if not data.get("ok"):
        return []

    admin_messages = []
    for update in data.get("result", []):
        _last_update_id = update["update_id"]
        msg = update.get("message", {})
        from_user = msg.get("from", {})
        if from_user.get("username") == ADMIN_USERNAME and msg.get("text"):
            admin_messages.append(msg["text"])

    return admin_messages


def wait_for_admin_reply(prompt_text, timeout_seconds=300):
    """Send a prompt to the admin and wait for their reply.

    Args:
        prompt_text: Message to send to the admin.
        timeout_seconds: How long to wait (default 5 minutes).

    Returns:
        The admin's reply text, or None if timed out.
    """
    import time

    send_message(prompt_text)

    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        messages = get_admin_messages()
        if messages:
            return messages[0]
        time.sleep(3)

    return None
