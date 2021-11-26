import os
from flask import Flask, render_template

from .db import mongo
from .dataseeder import seed_data
from .routes.app_bp import app_bp
from .routes.api_bp import api_bp
from .routes.admin_bp import admin_bp
from flask_session import Session

# Create Flask app and initialize mongodb connection
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
mongo.init_app(app, tlsAllowInvalidCertificates=True)

seed_data()

# Register blueprints
app.register_blueprint(app_bp, url_prefix="/")
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
