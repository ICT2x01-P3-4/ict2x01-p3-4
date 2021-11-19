from ...models.step import Step


def get_command():
    step = Step()
    command = step.get_next_step()
    direction = command["direction"]
    return f"Command: {direction}\0"
