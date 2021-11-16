import os
from flask import Flask, render_template

from .db import mongo
from .routes.app_bp import app_bp
from .routes.api_bp import api_bp
from .routes.admin_bp import admin_bp

# Create Flask app and initialize mongodb connection
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo.init_app(app, tlsAllowInvalidCertificates=True)

# Register blueprints
app.register_blueprint(app_bp, url_prefix="/")
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
