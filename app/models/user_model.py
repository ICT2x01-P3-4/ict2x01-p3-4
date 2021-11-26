import bcrypt
from flask import session, redirect, url_for
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

    def get_user(self) -> tuple:
        '''
        Get all users data from data base and display it for log in

        Returns:
            tuple: tuple of user data. 
            list[0] = name
            list[1] = stage
            list[2] = score 
        '''
        user_detail = self.user_db.find({'role': 'user'})
        user_detail = list(user_detail)
        name = []
        score = []
        stage = []
        for i in range(len(user_detail)):
            name.append(user_detail[i]['name'])
            score.append(user_detail[i]['score'])
            stage.append(user_detail[i]['stage'])
        return name, stage, score

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
            int: new updated score of user
        """
        score = self.user_db.find_one({'name': name}, {'score': 1})["score"]
        new_score = int(score) + 10
        self.user_db.update_one({'name': name}, {'$set': {'score': new_score}})
        return new_score

    def update_stage(self, name):
        """
        Increment the stage of user by 1.

        Args:
            name (string): name of user.

        Returns:
            int: new updated stage of user
        """
        stage = self.user_db.find_one({'name': name}, {'stage': 1})["stage"]
        new_stage = int(stage) + 1
        self.user_db.update_one({'name': name}, {'$set': {'stage': new_stage}})
        return new_stage
