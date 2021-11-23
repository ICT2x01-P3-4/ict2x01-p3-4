from .entities.car_entity import Car
from ..db import mongo


class CarModel:
    def __init__(self):
        self.car = mongo.db.car
        if self.car.find_one({}) is None:
            self.car.insert_one(Car().__dict__)

    def start(self):
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": True, "obstacle_detected": False}})

    def stop(self):
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": False, "obstacle_detected": False}})

    def detected_obstacle(self):
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": False, "obstacle_detected": True}})

    def is_moving(self):
        return self.car.find_one({})["is_moving"]
