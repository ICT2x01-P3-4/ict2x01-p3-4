import traceback
from flask import jsonify, request, session
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
        traceback.print_exc()
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
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def create_puzzle():
    """
    Creates a new puzzle in database.

    Returns:
        json: message and status code.
    """
    try:
        data = request.get_json()
        puzzle_model = PuzzleModel()
        new_puzzle_id = puzzle_model.create_puzzle(data)
        return jsonify({"message": f"New puzzle {new_puzzle_id} created"}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def update_puzzle(puzzle_id):
    """
    Updates a puzzle in database.

    Args:
            puzzle_id (int): puzzle id to be updated.

    Returns:
        json: puzzle data and status code.
    """
    try:
        data = request.get_json()
        puzzle_model = PuzzleModel()
        updated = puzzle_model.update_puzzle(puzzle_id, data)

        if not updated:
            return jsonify({"message": "Puzzle not found"}), 404

        return jsonify(data), 200
    except Exception as e:
        traceback.print_exc()
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
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def solve_puzzle(puzzle_id):
    """
    Checks for user's answer and executes all steps if correct.

    Updates user score and stage if answer is correct.

    Args:
        puzzle_id (string): puzzle id to be solved.
    Returns:
        json response: message and status code.
    """
    try:
        data = request.get_json()
        puzzle_model = PuzzleModel()
        done = puzzle_model.solve_puzzle(puzzle_id, data["steps"])

        if not done:
            return jsonify({"message": "Incorrect answer"}), 400

        user_model = UserModel()
        user_model.update_score(session["user"])
        user_model.update_stage(session["user"])

        return jsonify({"message": "Correct answer"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def step_through(puzzle_id):
    """
    Checks for user's answer and executes step.

    Update user score and stage if completed last step of puzzle.

    Args:
        puzzle_id (string): puzzle id to be stepped through.

    Returns:
        json response: message and status code.
    """
    try:
        data = request.get_json()
        puzzle_model = PuzzleModel()
        done = puzzle_model.step_through_puzzle(puzzle_id, data)

        if not done:
            return jsonify({"message": "Incorrect answer"}), 400

        if puzzle_model.at_last_step(puzzle_id, data):
            user = UserModel()
            user.update_score(session["user"])
            user.update_stage(session["user"])

        return jsonify({"message": "Step executed"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500