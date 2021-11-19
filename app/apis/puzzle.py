from flask import jsonify, request, session
import traceback

from app.models.Queue import Queue
from ..models.Puzzle import Puzzle
from ..models.User import User
from ..models.Step import Step


def get_puzzles():
    """
    Retrieve all puzzles from database.

    Returns:
        json: list of puzzles.
    """
    try:
        puzzle = Puzzle()
        puzzles = puzzle.get_all_puzzles()

        # Convert object id to string
        for puzzle in puzzles:
            puzzle["_id"] = str(puzzle["_id"])

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
        puzzle = Puzzle()
        puzzle_data = puzzle.get_puzzle(puzzle_id)
        puzzle_data["_id"] = str(puzzle_data["_id"])

        return jsonify(puzzle_data), 200
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
        puzzle = Puzzle(data)
        puzzle.create_puzzle(puzzle)

        return jsonify({"message": f"{puzzle.get_name()} created successfully"}), 201
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def update_puzzle():
    """
    Updates a puzzle in database.

    Returns:
        json: puzzle data and status code.
    """
    try:
        data = request.get_json()
        puzzle = Puzzle(data)
        updated = puzzle.update_puzzle(puzzle)

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
        puzzle = Puzzle()
        deleted = puzzle.delete_puzzle(puzzle_id)

        if not deleted:
            return jsonify({"message": "Puzzle not found"}), 404

        return jsonify({"message": "Puzzle deleted"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def execute_steps(steps):
    """
    Inserts steps into queue in db
    and wait for it to be emptied.

    Args:
        steps (list): list of steps.

    Returns:
        boolean: True when queue is emptied.
    """
    # Format steps into list of dicts
    steps_arr = []
    for i, step in enumerate(steps):
        steps_arr.append({"step_num": i+1, "direction": step})

    # Insert steps into queue
    queue = Queue()
    queue.create_queue(steps_arr)

    # Wait for queue to be emptied
    while True:
        if queue.get_queue_count() == 0:
            break

    return True


def at_last_step(puzzle, step):
    """
    Checks if user is at last step of puzzle.

    Args:
        puzzle (object): puzzle object.
        step (object): step object.

    Returns:
        boolean: True if current steps is last step of puzzle.
    """
    total_steps = len(puzzle["puzzle_steps"])
    return step["step_num"] == total_steps


def check_answer(puzzle, steps, is_solve):
    """
    Checks if answer is correct.

    First checks if user is solving or stepping through.
    Then checks if user's answer is same as solution.

    Args:
        puzzle (object): puzzle object.
        steps (list/object): steps to be executed.
        is_solve (boolean): True if solving puzzle, False if stepping through.

    Returns:
        boolean: True for correct answer, False for incorrect answer.
    """
    answer = puzzle["puzzle_steps"]

    if is_solve:
        if len(steps) != len(answer):
            return False

        for i, step in enumerate(steps):
            if step != answer[i]:
                return False
    else:
        if steps["step_num"] > len(answer):
            return False

        if steps["direction"] != answer[steps["step_num"]-1]:
            return False

    return True


def solve_puzzle():
    """
    Checks for user's answer and executes all steps if correct.

    Returns:
        json response: message and status code.
    """
    try:
        data = request.get_json()

        # Retrieve puzzle from db
        puzzle = Puzzle()
        puzzle_obj = puzzle.get_puzzle(data['puzzle_id'])

        # Check answer
        steps = data["steps"]
        is_correct = check_answer(puzzle_obj, steps, True)

        if not is_correct:
            return jsonify({"message": "Incorrect answer"}), 400

        done = execute_steps(steps)

        # Update user score and stage if completed execution on all steps of puzzle
        if done:
            user = User()
            user.update_score(session["user"])
            user.update_stage(session["user"])

        return jsonify({"message": "Correct answer"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def step_through():
    """
    Checks for user's answer and executes step.

    Returns:
        json response: message and status code.
    """
    try:
        data = request.get_json()

        # Retrieve puzzle from db
        puzzle = Puzzle()
        puzzle_obj = puzzle.get_puzzle(data['puzzle_id'])

        # Create step object and check answer
        step_obj = Step({"step_num": data["step_num"],
                         "direction": data["direction"]})
        is_correct = check_answer(puzzle_obj, step_obj, False)

        if not is_correct:
            return jsonify({"message": "Incorrect answer"}), 400

        done = execute_steps([step_obj])

        # Update user score and stage if completed last step of puzzle
        if done and at_last_step(puzzle_obj, step_obj):
            user = User()
            user.update_score(session["user"])
            user.update_stage(session["user"])

        return jsonify({"message": "Step executed"}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Something went wrong"}), 500
