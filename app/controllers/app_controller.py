from flask import render_template, redirect, url_for, request, session
from ..models.user_model import UserModel

def index():
    return render_template("index.html")

"""
def index():
    '''
    API to authenticate user from the database.
    The authentication does a HTTP GET request method to get 
    the information the user typed in, and does a POST request to the database to 
    verify the user. 
    '''
    if 'name' in session:
        return redirect(url_for("game_mode"))
    user = UserModel()
    name = request.form.get('name')
    
    in_session = user.login_user(name)

    if not in_session:
        return render_template("index.html")
    
    return redirect(url_for("game_mode"))
"""

def logout():
    '''
    Destroys the session the user is in
    and redirects back to index back. 
    '''
    user_model = UserModel()
    user_model.logout_user()
    return render_template("index.html")


def game_mode():
    return render_template("user_home.html")

def freestyle_mode():
    return render_template("freestyle_mode.html")

def puzzle_mode():
    return render_template("puzzle_mode.html")