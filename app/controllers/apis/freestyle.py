from typing import List
from ...models.user import User
from ...models.step import Step
import traceback
from typing import List
from flask import jsonify, request, session


def check_steps(steps: List, STEP_LIMIT: int) -> bool:
    '''
    Check the amount of steps satisfies the step limit. 

    Args:
        steps (list): list of steps from the robotic car

    Returns:
        bool: True if satisfy step limit
    '''

    if len(steps) <= STEP_LIMIT:
        return True
    else:
        return False


def execute_steps(steps: List) -> bool:
    """
    Inserts steps into queue in db
    and wait for it to be emptied.

    Args:
        steps (list): list of steps.

    Returns:
        boolean: True when queue is emptied.
    """
    if check_steps(steps, 15) == True:
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

    else:

        return False
