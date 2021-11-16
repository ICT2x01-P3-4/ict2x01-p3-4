from flask import Blueprint, app, render_template, redirect, url_for, request, flash, session
import bcrypt
from ...models import user

auth = Blueprint('admin_bp', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login_auth():
    message = 'Please login to your account'
    # if already logged in, start session
    if "username" in session:
        return redirect(url_for("login"))
