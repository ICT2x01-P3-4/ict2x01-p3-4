from .entities.car_entity import Car
from ..db import mongo


class CarModel:
    def __init__(self):
        self.car = mongo.db.car
        if self.car.find_one({}) is None:
            self.car.insert_one(Car().__dict__)

    def start(self):
        """
        Set is_moving to True and obstacle_detected to False

        Returns:
            object: result of the update
        """
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": True, "obstacle_detected": False}})

    def stop(self):
        """
        Set is_moving to False and obstacle_detected to False

        Returns:
            object: result of the update
        """
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": False, "obstacle_detected": False}})

    def detected_obstacle(self):
        """
        Set is_moving to False and obstacle_detected to True

        Returns:
            object: result of the update
        """
        return self.car.find_one_and_update(
            {}, {"$set": {"is_moving": False, "obstacle_detected": True}})

    def is_moving(self):
        """
        Get is_moving value

        Returns:
            boolean: True if car is moving, False otherwise
        """
        return self.car.find_one({})["is_moving"]
