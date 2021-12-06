from traceback import print_exc
from flask import request
from ..models.queue_model import QueueModel
from ..models.car_model import CarModel


def get_command():
    """
    Retrieve the first step in queue.

    Returns:
        string: Command to be executed.
    """
    try:
        queue = QueueModel()
        car = CarModel()
        direction = queue.get_next_step()

        if not direction or car.is_moving():
            return "None\0"

        return f"Command: {direction}\0"
    except Exception as e:
        print_exc()
        return "Failed\0"


def start_car():
    """
    Set the car to start.

    Returns:
        string: Status of the car.
    """
    try:
        car = CarModel()
        started = car.start()
        if not started:
            return 500
        return "Car started\0"
    except Exception as e:
        print_exc()
        return "Failed\0"


def stop_car():
    """
    Set the car to stop.

    Returns:
        string: Status of the car.
    """
    try:
        car = CarModel()
        queue = QueueModel()
        stopped = car.stop()

        if not stopped:
            return "Failed\0"

        queue.dequeue()
        return "Stopped\0"
    except Exception as e:
        print_exc()
        return "None\0"


def detected_obstacle():
    """
    Set the car detected obstacle status.

    Returns:
        string: Status of the car.
    """
    try:
        car = CarModel()
        detected_obstacle = car.detected_obstacle()
        if not detected_obstacle:
            return "Failed\0"
        return "Detected\0"
    except Exception as e:
        print_exc()
        return "None\0"


def insert_queue():
    """
    Insert the queue.

    Returns:
        string: Status of the car.
    """
    try:
        step = request.get_json()
        queue = QueueModel()
        queue.insert_to_queue(step)
        return "Inserted"
    except Exception as e:
        print_exc()
        return "Failed"
