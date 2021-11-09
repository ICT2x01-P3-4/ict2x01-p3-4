import os
from flask import Flask
from flask_pymongo import PyMongo
# from db import db

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app, tlsAllowInvalidCertificates=True)
db = mongo.db
