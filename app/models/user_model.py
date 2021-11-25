import bcrypt
from flask import session
from flask.helpers import url_for
from werkzeug.utils import redirect
from ..db import mongo


class UserModel:
    def __init__(self):
        self.user_db = mongo.db.users

    def login_admin(self, username, password) -> bool:
        '''
        API to authenticate user from the database.
        The authentication does a HTTP GET request method to get 
        the information the user typed in, and does a POST request to the database to 
        verify the user.

        Add-on features: bcrypt encryption for password hashing.  

        Returns:
            boolean: True if user is authenticated, False otherwise.
        '''
        user_detail = self.user_db.find_one({'username': username})
        if user_detail == None:
            return redirect(url_for('admin_bp.login'))
        if user_detail["role"] == "admin":
            # compare hashed password in db with password typed
            if bcrypt.checkpw(password.encode('utf-8'), user_detail['password']):
                session["username"] = user_detail['username']
                return True
            else:
                return False
        else:
            return False

    def login_user(self, user: str) -> bool:
        '''
        API to get user into session.

        Args:
            user(str): name of the user
        Returns:
            boolean: True if user is verified as user
        '''

        user_detail = self.user_db.find_one({'name': user})
        if user_detail['role'] == "user":
            session['name'] = user_detail
            return True
        return False

    def logout_user(self):
        '''
        Destroys the session the user is in
        and redirects back to index back.
        '''
        session.pop('user', None)

    def logout_admin(self):
        '''
        Destroys the session the user is in
        and redirects back to index back.
        '''
        session.pop("username", None)

    def update_score(self, name):
        """
        Increment the score of the user by 10.

        Args:
            name (string): name of user.

        Returns:
            object: result of update.
        """
        score = self.user_db.find_one({'name': name}, {'score': 1})
        new_score = score + 10
        return self.user_db.update_one({'name': name}, {'$set': {'score': new_score}})

    def update_stage(self, name):
        """
        Increment the stage of user by 1.

        Args:
            name (string): name of user.

        Returns:
            object: result of update.
        """
        stage = self.user_db.find_one({'name': name}, {'stage': 1})
        new_stage = stage + 1
        return self.user_db.update_one({'name': name}, {'$set': {'stage': new_stage}})
