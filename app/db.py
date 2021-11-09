import os
from flask import current_app
from flask_pymongo import PyMongo

def connectDB():
    mongo = PyMongo(current_app, tlsAllowInvalidCertificates=True)
    db = mongo.db
    return db

db = connectDB()