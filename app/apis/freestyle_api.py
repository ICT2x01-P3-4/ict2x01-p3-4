from flask import request, jsonify
from traceback import print_exc
from ..models.queue_model import QueueModel


def execute():
    """
    Insert steps to be executed into the queue.
    """
    try:
        queue = QueueModel()
        if not queue.is_empty():
            return jsonify({"error": "Queue is not empty"}), 400

        steps = request.get_json()["steps"]
        if not steps:
            return jsonify({"error": "No steps provided"}), 400

        queue.create_queue(steps)
        return jsonify({'message': "inserted"}), 200
    except Exception as e:
        print_exc()
        return jsonify({"error": "steps not inserted"}), 400


def check_queue():
    """
    Check if queue is empty.
    """
    try:
        queue = QueueModel()
        return jsonify({"is_empty": queue.is_empty()}), 200
    except Exception as e:
        print_exc()
        return jsonify({"error": str(e)}), 400
