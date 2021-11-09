import os
from flask import Flask
# from flask_pymongo import PyMongo
from .routes.api_bp import api_bp
from .routes.app_bp import app_bp

app = Flask(__name__)
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# mongo = PyMongo(app, tlsAllowInvalidCertificates=True)
# db = mongo.db

app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(app_bp, url_prefix="/")