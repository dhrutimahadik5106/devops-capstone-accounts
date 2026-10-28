
"""Account Management REST API with security headers."""

from flask import Flask, jsonify
from flask_talisman import Talisman

app = Flask(__name__)

# Configure security headers
csp = {
    "default-src": "'self'",
    "script-src": "'self'",
    "style-src": "'self'",
}

Talisman(
    app,
    content_security_policy=csp,
    force_https=False,
    frame_options="DENY",
    strict_transport_security=True,
    strict_transport_security_max_age=31536000,
    strict_transport_security_include_subdomains=True,
)

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200
