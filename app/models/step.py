from ..db import mongo


class Step:
    def __init__(self, step=None):
        if step is not None:
            self.step_num = step["step_num"]
            self.direction = step["direction"]
        self.step_queue_db = mongo.db.step_queue

    def get_step_num(self):
        return self.step_num

    def set_step_num(self, step_num):
        self.step_num = step_num

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction
