from ..db import mongo


class Step:
    def __init__(self, data=None):
        if data is not None:
            self.step_num = data["step_num"]
            self.direction = data["direction"]
        self.step_queue_db = mongo.db.step_queue

    def get_step_num(self):
        return self.step_num

    def set_step_num(self, step_num):
        self.step_num = step_num

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def create_queue(self, steps):
        self.step_queue_db.insert_many(steps)

    def get_queue_count(self):
        return self.step_queue_db.count()
