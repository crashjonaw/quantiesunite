"""Payment routes — HitPay integration for plan purchases."""

import os
import hmac
import hashlib
import json
import subprocess
from flask import Blueprint, request, jsonify, redirect, flash, url_for, session
from routes.helpers import current_user, login_required
import database as db

payments_bp = Blueprint("payments", __name__)

HITPAY_API_URL = "https://api.hit-pay.com/v1"

# Load from .env file directly (in case env vars aren't exported)
_env_cache = {}
def _load_env():
    if not _env_cache:
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, val = line.split("=", 1)
                        _env_cache[key.strip()] = val.strip()
    return _env_cache

def _get_api_key():
    return os.environ.get("HITPAY_API_KEY") or _load_env().get("HITPAY_API_KEY", "")

def _get_salt():
    return os.environ.get("HITPAY_SALT") or _load_env().get("HITPAY_SALT", "")

# Plan pricing
PLAN_PRICES = {
    "primary":   {"1_month": 9.90,  "3_months": 24.90,  "1_year": 79.90},
    "secondary": {"1_month": 14.90, "3_months": 39.90,  "1_year": 119.90},
    "jc":        {"1_month": 19.90, "3_months": 49.90,  "1_year": 159.90},
    "full":      {"1_month": 24.90, "3_months": 64.90,  "1_year": 199.90},
}

PLAN_NAMES = {
    "primary": "Primary", "secondary": "Secondary",
    "jc": "JC / A-Level", "full": "Full Programme",
}

DURATION_NAMES = {
    "1_month": "1 Month", "3_months": "3 Months", "1_year": "1 Year",
}


@payments_bp.route("/api/payments/create", methods=["POST"])
@login_required
def create_payment():
    """Create a HitPay payment request and return the checkout URL."""
    user = current_user()
    data = request.get_json()
    tier = data.get("tier", "")
    duration = data.get("duration", "")

    if tier not in PLAN_PRICES or duration not in PLAN_PRICES.get(tier, {}):
        return jsonify({"ok": False, "error": "Invalid plan selection."}), 400

    amount = PLAN_PRICES[tier][duration]
    plan_name = PLAN_NAMES.get(tier, tier)
    duration_name = DURATION_NAMES.get(duration, duration)

    # Build reference: user_id|tier|duration
    reference = f"{user['id']}|{tier}|{duration}"

    # Create HitPay payment request via curl (same approach as Google OAuth)
    redirect_url = request.host_url.rstrip("/") + "/payment/success"
    webhook_url = request.host_url.rstrip("/") + "/api/hitpay/webhook"

    try:
        result = subprocess.run([
            "curl", "-s", "-X", "POST",
            f"{HITPAY_API_URL}/payment-requests",
            "-H", f"X-BUSINESS-API-KEY: {_get_api_key()}",
            "-H", "Content-Type: application/x-www-form-urlencoded",
            "-d", f"amount={amount:.2f}",
            "-d", "currency=SGD",
            "-d", f"email={user['email']}",
            "-d", f"name={user['username']}",
            "-d", f"purpose=QuantiesUnite {plan_name} - {duration_name}",
            "-d", f"reference_number={reference}",
            "-d", f"redirect_url={redirect_url}",
            "-d", f"webhook={webhook_url}",
        ], capture_output=True, text=True, timeout=15)

        resp = json.loads(result.stdout)

        if "url" in resp:
            return jsonify({"ok": True, "url": resp["url"]})
        else:
            error = resp.get("message", resp.get("error", "Unknown error"))
            return jsonify({"ok": False, "error": str(error)}), 400

    except Exception as e:
        return jsonify({"ok": False, "error": f"Payment service error: {str(e)}"}), 500


@payments_bp.route("/api/hitpay/webhook", methods=["POST"])
def hitpay_webhook():
    """Handle HitPay webhook — auto-activate plan on successful payment."""
    data = request.form.to_dict()

    # Verify HMAC signature
    salt = _get_salt()
    if salt:
        # HitPay signs with specific fields in alphabetical order
        sign_fields = sorted([
            k for k in data.keys()
            if k != "hmac" and data[k] != ""
        ])
        sign_string = "|".join(str(data[k]) for k in sign_fields)
        expected_hmac = hmac.new(
            salt.encode(), sign_string.encode(), hashlib.sha256
        ).hexdigest()

        if data.get("hmac") != expected_hmac:
            return jsonify({"error": "Invalid signature"}), 401

    # Check payment status
    status = data.get("status", "")
    if status != "completed":
        # Payment not completed — ignore
        return jsonify({"ok": True, "status": "ignored"})

    # Parse reference: user_id|tier|duration
    reference = data.get("reference_number", "")
    parts = reference.split("|")
    if len(parts) != 3:
        return jsonify({"error": "Invalid reference"}), 400

    try:
        user_id = int(parts[0])
        tier = parts[1]
        duration = parts[2]
    except (ValueError, IndexError):
        return jsonify({"error": "Invalid reference format"}), 400

    # Validate tier and duration
    if tier not in PLAN_PRICES or duration not in PLAN_PRICES.get(tier, {}):
        return jsonify({"error": "Invalid plan in reference"}), 400

    amount = float(data.get("amount", 0))
    payment_id = data.get("payment_request_id", "")

    # Activate the plan
    db.activate_plan(
        user_id=user_id,
        plan_tier=tier,
        plan_duration=duration,
        amount_paid=amount,
        payment_ref=payment_id,
        activated_by="hitpay_webhook"
    )

    return jsonify({"ok": True, "status": "activated"})
