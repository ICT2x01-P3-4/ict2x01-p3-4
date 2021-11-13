class Step:
    def __init__(self, step_num, direction):
        self.step_num = step_num
        self.direction = direction

    def get_step_num(self):
        return self.step_num

    def set_step_num(self, step_num):
        self.step_num = step_num

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction
