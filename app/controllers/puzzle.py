from ..models.puzzle import Puzzle
from ..models.step import Step
from ..models.user import User
from flask import jsonify, request, session, render_template


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
    steps_arr_obj = []
    for i, step in enumerate(steps):
        steps_arr_obj.append({"step_num": i+1, "direction": step})

    # Insert steps into queue
    step = Step()
    step.create_queue(steps_arr_obj)

    # Wait for queue to be emptied
    while True:
        if step.get_queue_count() == 0:
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
        print(e)
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
        step_obj = {"step_num": data["step_num"],
                    "direction": data["direction"]}
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
        print(e)
        return jsonify({"message": "Something went wrong"}), 500


def puzzle_mode():
    return render_template("puzzle_mode.html")
