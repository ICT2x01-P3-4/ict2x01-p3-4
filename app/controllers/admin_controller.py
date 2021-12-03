from ..models.puzzle_model import PuzzleModel
from ..models.user_model import UserModel
from flask import render_template, redirect, url_for, request, session, flash


def index():
    if not session.get('username'):
        return redirect(url_for('admin_bp.login'))
    return render_template('admin/index.html')


def profile():
    if not session.get('username'):
        return redirect(url_for('admin_bp.login'))
    user_model = UserModel()
    users = user_model.get_all_users()
    admin = user_model.get_admin_account()
    return render_template('admin/profile.html', admin=admin, users=users)


def puzzle():
    if not session.get('username'):
        return redirect(url_for('admin_bp.login'))
    puzzle_model = PuzzleModel()
    length = len(puzzle_model.get_all_puzzles())
    return render_template('admin/puzzle.html', puzzles=puzzle_model.get_all_puzzles(), length = length)


def edit_puzzle(puzzle_id):
    if not session.get('username'):
        return redirect(url_for('admin_bp.login'))
    puzzle_model = PuzzleModel()
    return render_template('admin/edit_puzzle.html', puzzle=puzzle_model.get_puzzle(puzzle_id))


def create_puzzle():
    if not session.get('username'):
        return redirect(url_for('admin_bp.login'))
    return render_template('admin/create_puzzle.html')


def login_post() -> bool:
    '''
    Gets request form data and validate admin information

    Returns:
        boolean: True if admin information is verified and False if not verified 
    '''
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
        if auth:
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
