from flask import render_template, redirect, url_for, request, session
from ..models.user_model import UserModel


def index():
    if request.method == "GET":
        colors = ['bg-blue-300', 'bg-indigo-300', 'bg-purple-300',
                  'bg-blue-300', 'bg-indigo-300', 'bg-purple-300']
        colors_hover = ['bg-blue-200', 'bg-indigo-200', 'bg-purple-200',
                        'bg-blue-200', 'bg-indigo-200', 'bg-purple-200']
        user = UserModel()
        name = user.get_user()
        name = name[0]
        len_name = len(name)
        # for name, 0 index is name, 2nd index is stage, 2nd index is score
        return render_template("index.html", color=colors, colors_hover=colors_hover,
                               name=name, len_name=len_name)
    elif request.method == "POST":
        valid = index_post()
        if valid == True:
            return redirect(url_for('app_bp.game_mode'))
        else:
            return redirect(url_for('app_bp.index'))


def index_post() -> bool:
    '''
    Gets request form data and validate user information

    Returns:
        boolean: True if user information is verified and False if not verified 
    '''
    name = request.form.get('name')
    user = UserModel()
    user_details = user.login_user(name)
    return user_details


def logout():
    '''
    Destroys the session the user is in
    and redirects back to index back. 
    '''
    user_model = UserModel()
    user_model.logout_user()
    return redirect(url_for('app_bp.index'))


def game_mode():
    if "name" not in session:
        return redirect(url_for('app_bp.index'))

    user_session = session['name']
    return render_template("user_home.html", user=user_session['name'], score=user_session['score'])


def freestyle_mode():
    return render_template("freestyle_mode.html")


def puzzle_mode():
    return render_template("puzzle_mode.html")
