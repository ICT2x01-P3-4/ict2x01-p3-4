from traceback import print_exc
from flask import jsonify, request, session, redirect
from flask.helpers import url_for

from ..models.queue_model import QueueModel
from ..models.puzzle_model import PuzzleModel
from ..models.user_model import UserModel


def get_puzzles():
    """
    Retrieve all puzzles from database.

    Returns:
        json: list of puzzles.
    """
    try:
        puzzle_model = PuzzleModel()
        puzzles = puzzle_model.get_all_puzzles()

        return jsonify(puzzles), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def get_puzzle_by_id(puzzle_id):
    """
    Retrieve a puzzle from database.

    Args:
        puzzle_id (int): puzzle id to be retrieved.

    Returns:
        json: puzzle object data
    """
    try:
        puzzle_model = PuzzleModel()
        puzzle = puzzle_model.get_puzzle(puzzle_id)

        return jsonify(puzzle), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def create_puzzle():
    """
    Creates a new puzzle in database.

    Check for validation before moving on
    to creation.

    Returns:
        json: message and status code.
    """
    try:
        data = request.get_json()
        puzzle_model = PuzzleModel()

        validated = puzzle_model.validate_puzzle(data)
        if not validated:
            return jsonify({"message": "Invalid puzzle data"}), 400

        created = puzzle_model.create_puzzle(data)
        if not created:
            return jsonify({"message": "Puzzle already exists"}), 400

        return jsonify({"message": "Puzzle created"}), 201
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def update_puzzle(puzzle_id):
    """
    Updates a puzzle in database.

    Checks for validation before moving on
    to update.

    Args:
        puzzle_id (int): puzzle id to be updated.

    Returns:
        json: puzzle data and status code.
    """
    try:
        data = request.get_json()
        puzzle_model = PuzzleModel()

        validated = puzzle_model.validate_puzzle(data)
        if not validated:
            return jsonify({"message": "Invalid puzzle data"}), 400

        updated = puzzle_model.update_puzzle(puzzle_id, data)
        if not updated:
            return jsonify({"message": "Puzzle not found"}), 404

        return jsonify(data), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def delete_puzzle(puzzle_id):
    """
    Deletes a puzzle from database.

    Args:
        puzzle_id (int): puzzle id to be deleted.

    Returns:
        json: message and status code.
    """
    try:
        puzzle = PuzzleModel()
        deleted = puzzle.delete_puzzle(puzzle_id)

        if not deleted:
            return jsonify({"message": "Puzzle not found"}), 404

        return jsonify({"message": "Puzzle deleted"}), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def solve_puzzle(puzzle_id):
    """
    Checks for correct answer and insert steps into queue.

    Checks if queue is empty before inserting.

    Args:
        puzzle_id (string): puzzle id to be solved.
    Returns:
        json response: message and status code.
    """
    try:
        queue = QueueModel()
        if not queue.is_empty():
            return jsonify({"message": "Car is still executing!", "icon": "warning"}), 400

        data = request.get_json()
        puzzle_model = PuzzleModel()
        done = puzzle_model.solve_puzzle(puzzle_id, data["steps"])

        if not done:
            return jsonify({"message": "Incorrect answer. Please try again.", "icon": "error"}), 400

        return jsonify({"message": "Correct answer"}), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def step_through(puzzle_id):
    """
    Checks for user's answer and insert a step into the queue.

    Checks if queue is empty before inserting.

    Args:
        puzzle_id (string): puzzle id to be stepped through.

    Returns:
        json response: message and status code.
    """
    try:
        data = request.get_json()
        step = data["step"]
        queue = QueueModel()

        if not queue.is_empty():
            return jsonify({"message": "Car is still executing!", "icon": "warning"}), 400

        puzzle_model = PuzzleModel()
        done = puzzle_model.step_through_puzzle(puzzle_id, step)

        if not done:
            return jsonify({"message": "Incorrect answer"}), 400

        return jsonify({"message": "Step executed"}), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def check_puzzle_queue():
    """
    Checks if queue is empty, if not, return
    current queue as array.

    Returns:
        json: message/array and status code.
    """
    try:
        queue = QueueModel()
        if queue.is_empty():
            return jsonify({"is_empty": True}), 200

        queue_arr = queue.get_queue_arr()
        return jsonify({"queue": queue_arr}), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def update_score():
    """
    Increment stage and score of current user.

    Returns:
        json: message and status code.
    """
    try:
        if "user" in session:
            user = UserModel()
            puzzle_model = PuzzleModel()
            name = session["user"]["name"]
            user.update_score(name)
            new_stage = user.update_stage(name)
            session["user"] = user.get_user_details(name)

            if new_stage == puzzle_model.get_puzzles_count():
                return redirect(url_for("app_bp.puzzle_mode"))

            return jsonify({"message": "Score updated"}), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def get_total_puzzles():
    """
    Get total number of puzzles.

    Returns:
        json: puzzle count.
    """
    try:
        puzzle_model = PuzzleModel()
        return jsonify({"total": puzzle_model.get_puzzles_count()}), 200
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500
