from flask import Blueprint, app, render_template, redirect, url_for, request, flash, session
import bcrypt
from ...db import mongo
from ...models import user


def login_auth():
    '''
    API to authenticate user from the database.
    The authentication does a HTTP GET request method to get 
    the information the user typed in, and does a POST request to the database to 
    verify the user.

    Add-on features: bcrypt encryption for password hashing.  
    '''

    admins = mongo.db.users
    message = 'Please login to your account'
    # if already logged in, start session
    if "username" in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_found = admins.findone({"username": username})
        admin_verify = admins.find_one({"role": "admin"})

        # if username is found inside the database
        if user_found:
            if admin_verify:
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
                message = "You are not an admin"
                return render_template('admin/login.html', message=message)
        else:
            message = 'Username is not found'
            return render_template('admin/login.html', message=message)
        return render_template('admin/login.html', message=message)
