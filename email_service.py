"""
Email service — send welcome and notification emails via Gmail SMTP.
"""

import smtplib
import os
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def _get_creds():
    """Load Gmail credentials from env or .env file."""
    user = os.environ.get("GMAIL_USER")
    pwd = os.environ.get("GMAIL_APP_PASSWORD")
    if user and pwd:
        return user, pwd
    # Fallback: read .env file
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            env = {}
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
            return env.get("GMAIL_USER", ""), env.get("GMAIL_APP_PASSWORD", "")
    return "", ""


def _send_email(to_email, subject, html_body):
    """Send an email via Gmail SMTP. Runs in background thread."""
    gmail_user, gmail_pwd = _get_creds()
    if not gmail_user or not gmail_pwd:
        return

    msg = MIMEMultipart("alternative")
    msg["From"] = f"QuantiesUnite <{gmail_user}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_pwd)
            server.send_message(msg)
    except Exception as e:
        import logging
        logging.error(f"Failed to send email to {to_email}: {e}")


def send_async(to_email, subject, html_body):
    """Send email in a background thread so it doesn't block the request."""
    thread = threading.Thread(target=_send_email, args=(to_email, subject, html_body))
    thread.daemon = True
    thread.start()


def send_promo_email(username, email):
    """Send a welcome email with promo announcement to a new user."""
    subject = f"Welcome to QuantiesUnite, {username}! 🎁 You've unlocked full access!"
    html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 560px; margin: 0 auto; padding: 32px 24px; color: #333;">

      <div style="text-align: center; margin-bottom: 28px;">
        <h1 style="font-size: 1.6rem; font-weight: 800; margin: 0;">
          <span style="color: #4169E1;">Q</span>uanties<span style="color: #FF4500;">Unite</span>
        </h1>
      </div>

      <h2 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 12px;">Welcome aboard, {username}!</h2>

      <div style="background: linear-gradient(135deg, #4169E1, #7B68EE); color: #fff; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; text-align: center;">
        <div style="font-size: 1.8rem; margin-bottom: 6px;">🎁</div>
        <div style="font-size: 1.1rem; font-weight: 800;">You're one of our first 30 users!</div>
        <div style="font-size: 0.95rem; margin-top: 6px;">You've been given <strong>1 month of Full Programme access — completely free</strong>.</div>
      </div>

      <p style="font-size: 0.95rem; line-height: 1.7; color: #555; margin-bottom: 16px;">
        As an early supporter, you now have access to our <strong>entire curriculum</strong> for 30 days — no payment required. Here's what's unlocked for you:
      </p>

      <ul style="font-size: 0.93rem; line-height: 1.8; color: #555; padding-left: 20px; margin-bottom: 20px;">
        <li><strong>Kindergarten to Primary 6</strong> — Numbers, fractions, decimals, PSLE prep</li>
        <li><strong>Secondary 1–4</strong> — Algebra, trigonometry, E-Math &amp; A-Math</li>
        <li><strong>JC / A-Level</strong> — Complex numbers, calculus, vectors, statistics</li>
        <li><strong>University</strong> — Linear algebra, probability, Python</li>
        <li><strong>Deep Learning</strong> — Neural networks, LSTM, attention, transformers</li>
        <li><strong>101 topics</strong>, <strong>7,300+ questions</strong>, <strong>6 grade exams</strong></li>
      </ul>

      <div style="text-align: center; margin: 28px 0;">
        <a href="https://quantiesunite.sg/curriculum"
           style="display: inline-block; background: #4169E1; color: #fff; padding: 14px 36px; border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 0.95rem;">
          Start Exploring →
        </a>
      </div>

      <p style="font-size: 0.88rem; line-height: 1.6; color: #888; margin-bottom: 8px;">
        Your full access expires in 30 days. After that, you can continue with a paid plan starting from S$7.90/month.
      </p>

      <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

      <p style="font-size: 0.78rem; color: #aaa; text-align: center; margin: 0;">
        Made in Singapore with love for learning<br>
        <a href="https://quantiesunite.sg" style="color: #4169E1; text-decoration: none;">quantiesunite.sg</a>
      </p>

    </div>
    """
    send_async(email, subject, html)


def send_welcome_email(username, email):
    """Send a welcome email to a new user."""
    subject = f"Welcome to QuantiesUnite, {username}!"
    html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 560px; margin: 0 auto; padding: 32px 24px; color: #333;">

      <div style="text-align: center; margin-bottom: 28px;">
        <h1 style="font-size: 1.6rem; font-weight: 800; margin: 0;">
          <span style="color: #4169E1;">Q</span>uanties<span style="color: #FF4500;">Unite</span>
        </h1>
      </div>

      <h2 style="font-size: 1.3rem; font-weight: 700; margin: 0 0 12px;">Welcome aboard, {username}!</h2>

      <p style="font-size: 0.95rem; line-height: 1.7; color: #555; margin-bottom: 16px;">
        Thank you for joining QuantiesUnite! You're now part of a learning community that teaches mathematics from first principles — from Kindergarten all the way to Deep Learning.
      </p>

      <p style="font-size: 0.95rem; line-height: 1.7; color: #555; margin-bottom: 16px;">
        Here's what you can do right now:
      </p>

      <ul style="font-size: 0.93rem; line-height: 1.8; color: #555; padding-left: 20px; margin-bottom: 20px;">
        <li><strong>Explore the Curriculum</strong> — 101 topics across 12 levels</li>
        <li><strong>Take Quizzes</strong> — 7,300+ practice questions with instant feedback</li>
        <li><strong>Track Your Progress</strong> — Dashboard, trophies, and milestones</li>
        <li><strong>View the Topic Graph</strong> — See how every concept connects</li>
      </ul>

      <div style="text-align: center; margin: 28px 0;">
        <a href="https://quantiesunite.sg/curriculum"
           style="display: inline-block; background: #4169E1; color: #fff; padding: 14px 36px; border-radius: 10px; text-decoration: none; font-weight: 700; font-size: 0.95rem;">
          Start Learning →
        </a>
      </div>

      <p style="font-size: 0.88rem; line-height: 1.6; color: #888; margin-bottom: 8px;">
        Every topic starts with "why" — so you understand, not just memorize.
      </p>

      <hr style="border: none; border-top: 1px solid #eee; margin: 24px 0;">

      <p style="font-size: 0.78rem; color: #aaa; text-align: center; margin: 0;">
        Made in Singapore with love for learning<br>
        <a href="https://quantiesunite.sg" style="color: #4169E1; text-decoration: none;">quantiesunite.sg</a>
      </p>

    </div>
    """
    send_async(email, subject, html)
