from flask import render_template, redirect, url_for, request, session
from ..models.user_model import UserModel


def index():
    if 'name' in session:
        return redirect(url_for("game_mode"))
    user = UserModel()
    name = request.form.get('name')
    in_session = user.login_user(name)

    if not in_session:
        return render_template("index.html")
    return redirect(url_for("game_mode"))


def game_mode():
    return render_template("userhome.html")
