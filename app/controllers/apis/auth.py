from flask import Blueprint, app, render_template, redirect, url_for, request, flash, session
import bcrypt
import pymongo
import os
from ...models import user

auth = Blueprint('admin_bp', __name__)


client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client.get_database('admins')
admins = db.register


@auth.route('/login', methods=['POST', 'GET'])
def login_auth():
    message = 'Please login to your account'
    # if already logged in, start session
    if "username" in session:
        return redirect(url_for("login"))
