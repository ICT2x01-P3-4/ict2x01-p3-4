from ..models.puzzle import Puzzle
from ..models.step import Step
from flask import jsonify, request


def execute_step_through():
    try:
        pass
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500


def execute_steps(steps):
    """
    Inserts steps into queue in db
    and wait for it to be emptied.
    """
    # Format steps into list of dicts
    steps_arr_obj = []
    for i, step in enumerate(steps):
        steps_arr_obj.append({"step_num": i+1, "direction": step})

    # Insert steps into queue`
    step = Step()
    step.create_queue(steps_arr_obj)

    # Wait for queue to be emptied
    while True:
        if step.get_queue_count() == 0:
            break

    return True


def check_answer(puzzle, steps):
    """
    Checks if steps is same as answer
    """
    answer = puzzle["puzzle_steps"]

    if len(steps) != len(answer):
        return False

    for i, step in enumerate(steps):
        if step != answer[i]:
            return False

    return True


def solve_puzzle():
    """
    Solves a puzzle and executes the action.
    """
    try:
        data = request.get_json()
        steps = data["steps"]
        puzzle = Puzzle()
        puzzle_obj = puzzle.get_puzzle(data['puzzle_id'])
        is_correct = check_answer(puzzle_obj, steps)

        if not is_correct:
            return jsonify({"message": "Incorrect answer"}), 400

        done = execute_steps(steps)
        # TODO: update score
        # TODO: update stage
        return jsonify({"message": "Correct answer"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500
