import traceback
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
        step = queue.get_next_step()
        command = step["direction"]
        if command:
            return f"Command: {command}\0"
        else:
            return "None\0"
    except Exception as e:
        traceback.print_exc()
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
            return "Failed\0"
        return "Started\0"
    except Exception as e:
        traceback.print_exc()
        return "Failed\0"


def stop_car():
    """
    Set the car to stop.

    Returns:
        string: Status of the car.
    """
    try:
        car = CarModel()
        stopped = car.stop()
        if not stopped:
            return "Failed\0"
        return "Stopped\0"
    except Exception as e:
        traceback.print_exc()
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
        traceback.print_exc()
        return "None\0"
