from .entities.user_entity import User
from ..db import mongo


class UserModel:
    def __init__(self):
        self.user_db = mongo.db.users

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
