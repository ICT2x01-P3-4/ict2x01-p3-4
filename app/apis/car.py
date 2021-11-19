import traceback
from ..models.Queue import Queue
from ..models.Car import Car


def get_command():
    try:
        queue = Queue()
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
    try:
        car = Car()
        started = car.start()
        if not started:
            return "Failed\0"
        return "Started\0"
    except Exception as e:
        traceback.print_exc()
        return "Failed\0"


def stop_car():
    try:
        car = Car()
        stopped = car.stop()
        if not stopped:
            return "Failed\0"
        return "Stopped\0"
    except Exception as e:
        traceback.print_exc()
        return "None\0"


def detected_obstacle():
    try:
        car = Car()
        detected_obstacle = car.detected_obstacle()
        if not detected_obstacle:
            return "Failed\0"
        return "Detected\0"
    except Exception as e:
        traceback.print_exc()
        return "None\0"
