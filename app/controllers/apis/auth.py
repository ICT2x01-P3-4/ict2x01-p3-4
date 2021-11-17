from flask import Blueprint, app, render_template, redirect, url_for, request, flash, session
import bcrypt
import pymongo
import os
from ...models import user

auth = Blueprint('admin_bp', __name__)


client = pymongo.MongoClient(os.environ.get("MONGO_URI"))


def login_auth(db):
    '''
    API to authenticate user from the database.
    The authentication does a HTTP GET request method to get 
    the information the user typed in, and does a POST request to the database to 
    verify the user.

    Add-on features: bcrypt encryption for password hashing.  
    '''

    # Declaration of database
    db = client.get_database('admins')
    admins = db.register
    message = 'Please login to your account'
    # if already logged in, start session
    if "username" in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_found = admins.findone({"username": username})
        # if username is found inside the database
        if user_found:
            user_valid = user_found['username']
            password_check = user_found['password']

            # compare hashed password in db with password typed
            if bcrypt.checkpw(password.encode('utf-8'), password_check):
                session["username"] = user_valid
                return redirect(url_for("login"))

            else:
                if "username" in session:
                    return redirect(url_for("login"))
                message = 'Wrong Password'
                return render_template('admin/login.html', message=message)

        else:
            message = 'Username is not found'
            return render_template('admin/login.html', message=message)
        return render_template('admin/login.html', message=message)
