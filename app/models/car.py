from ..db import mongo


class Car:
    def __init__(self, car=None):
        if car is not None:
            self.id = car["id"]
            self.distance = car["distance"]
            self.total_distance = car["total_distance"]
            self.is_moving = car["is_moving"]
            self.move = car["move"]
            self.obstacle = car["obstacle"]
        self.car = mongo.db.car
        if self.car.find_one({}) is None:
            self.car.insert_one({"is_moving": False, "obstacle": False})

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

    def start(self):
        return self.car.find_one_and_update(
            {"id": "0"}, {"$set": {"is_moving": True, "obstacle": False}})

    def stop(self):
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": False, "obstacle": False}})

    def detected_obstacle(self):
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": False, "obstacle": True}})
