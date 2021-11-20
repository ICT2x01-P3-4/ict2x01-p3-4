import bcrypt
from ..db import mongo
from ..models.puzzle_model import PuzzleModel
from flask import render_template, redirect, url_for, request, session


def index():
    return render_template('admin/index.html')


def profile():
    return render_template('admin/profile.html')


def puzzle():
    puzzle_model = PuzzleModel()
    return render_template('admin/puzzle.html', puzzles=puzzle_model.get_all_puzzles())


def edit_puzzle(puzzle_id):
    puzzle_model = PuzzleModel()
    return render_template('admin/edit_puzzle.html', puzzle=puzzle_model.get_puzzle(puzzle_id))


def create_puzzle():
    return render_template('admin/create_puzzle.html')


def login():
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
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_detail = admins.find_one({"username": username})

        # if username is found inside the database
        if user_detail["role"] == "admin":
            user_detail = user_detail['username']
            pwd = user_detail['password']

            # compare hashed password in db with password typed
            if bcrypt.checkpw(password.encode('utf-8'), pwd):
                session["username"] = user_detail
                return redirect(url_for("index"))

            else:
                if "username" in session:
                    return redirect(url_for("index"))
                message = 'Wrong Password'
                return render_template('admin/login.html', message=message)

        else:
            message = 'Username is not found'
            return render_template('admin/login.html', message=message)
        return render_template('admin/login.html', message=message)


def logout():
    '''
    Destroys the session the user is in
    and redirects back to index back. 
    '''
    if "username" in session:
        session.pop("username", None)
    render_template("admin/index.html")
