from flask import render_template, redirect, url_for, request, session
from ..models.user_model import UserModel


def index():

    colors = ['bg-blue-300', 'bg-indigo-300', 'bg-purple-300',
              'bg-blue-300', 'bg-indigo-300', 'bg-purple-300']
    colors_hover = ['bg-blue-200', 'bg-indigo-200', 'bg-purple-200',
                    'bg-blue-200', 'bg-indigo-200', 'bg-purple-200']
    user = UserModel()
    name = user.get_user()
    name = name[0]
    len_name = len(name)
    print(name)
    # for name, 0 index is name, 2nd index is stage, 2nd index is score
    return render_template("index.html", color=colors, colors_hover=colors_hover, 
    name=name, len_name = len_name)


def index_post():
    pass


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
