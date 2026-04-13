"""
QuantiesUnite — Route Blueprints

Registers all blueprints with the Flask app.
"""

from routes.auth import auth_bp
from routes.account import account_bp
from routes.dashboard import dashboard_bp
from routes.admin import admin_bp
from routes.learning import learning_bp
from routes.exam import exam_bp
from routes.payments import payments_bp


def register_blueprints(app):
    """Register all route blueprints with the Flask app."""
    app.register_blueprint(auth_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(learning_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(payments_bp)
