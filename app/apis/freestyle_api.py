from flask import request
from ..models.queue_model import QueueModel


def execute():
    """
    Insert steps to be executed into the queue.
    """
    steps = request.get_json()
    print(steps)
    # queue = QueueModel()
    # queue.create_queue(steps)
