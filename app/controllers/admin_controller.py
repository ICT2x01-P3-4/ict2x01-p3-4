from ..models.puzzle_model import PuzzleModel
from ..models.user_model import UserModel
from flask import render_template, redirect, url_for, request, session, flash
from ..db import mongo


def index():
    if not session.get('username'):
        return redirect(url_for('admin_bp.login'))
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


def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = UserModel()
    user_details = user.login_admin(username, password)
    return user_details


def login():
    if request.method == "GET":
        return render_template('admin/login.html')
    elif request.method == "POST":
        auth = login_post()
        if auth == True:
            return redirect(url_for('admin_bp.index'))
        else:
            flash("Please check your Login details and try again")
            return redirect(url_for('admin_bp.login'))


def logout():
    '''
    Destroys the session the user is in
    and redirects back to index back. 
    '''
    user_model = UserModel()
    user_model.logout_admin()
    return redirect(url_for('admin_bp.login'))
