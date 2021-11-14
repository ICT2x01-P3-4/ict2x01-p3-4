import os
from flask import Flask

from .db import mongo
from .routes.app_bp import app_bp
from .routes.puzzle_bp import puzzle_bp

# Create Flask app and initialize mongodb connection
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo.init_app(app, tlsAllowInvalidCertificates=True)

# Register blueprints
app.register_blueprint(app_bp, url_prefix="/")
app.register_blueprint(puzzle_bp, url_prefix="/puzzle")
