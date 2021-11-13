class Car:
    def __init__(self, distance, total_distance, is_moving, move, obstacle):
        self.distance = distance
        self.total_distance = total_distance
        self.is_moving = is_moving
        self.move = move
        self.obstacle = obstacle

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def get_total_distance(self):
        return self.total_distance

    def set_total_distance(self, total_distance):
        self.total_distance = total_distance

    def get_is_moving(self):
        return self.is_moving

    def set_is_moving(self, is_moving):
        self.is_moving = is_moving

    def get_move(self):
        return self.move

    def set_move(self, move):
        self.move = move

    def get_obstacle(self):
        return self.obstacle

    def set_obstacle(self, obstacle):
        self.obstacle = obstacle
