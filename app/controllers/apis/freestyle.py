from typing import List
from ...models.user import User
from ...models.step import Step
import traceback
from flask import jsonify, request, session


def execute_steps(steps: List) -> bool:
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
    queue_flag = True
    while queue_flag == True:
        if step.get_queue_count() == 0:
            queue_flag = False

    return True
