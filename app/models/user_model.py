from ..db import mongo


class User:
    def __init__(self, user=None):
        if user is not None:
            self.name = user['name']
            self.score = user['score']
            self.stage = user['stage']
        self.user_db = mongo.db.users

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_stage(self):
        return self.stage

    def set_stage(self, stage):
        self.stage = stage

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
