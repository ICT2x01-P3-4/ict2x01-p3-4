from ..models.puzzle_model import PuzzleModel
from ..models.user_model import UserModel
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
    '''

    if "username" in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_model = UserModel()
        is_authenticated = user_model.login_admin(username, password)

        if not is_authenticated:
            message = 'Wrong Username/Password'
            return render_template('admin/login.html', message=message)

        return redirect(url_for("index"))

    message = 'Please login to your account'
    return render_template('admin/login.html', message=message)


def logout():
    '''
    Destroys the session the user is in
    and redirects back to index back. 
    '''
    user_model = UserModel()
    user_model.logout_admin()
    render_template("admin/index.html")
