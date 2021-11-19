from ..db import mongo


class Step:
    def __init__(self, step=None):
        if step is not None:
            self.step_num = step["step_num"]
            self.direction = step["direction"]
        self.step_queue_db = mongo.db.step_queue

    def get_step_num(self):
        return self.step_num

    def set_step_num(self, step_num):
        self.step_num = step_num

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def create_queue(self, steps):
        """
        Insert a list of steps into the queue.

        Args:
            steps (list): list of steps to insert into the queue.
        """
        self.step_queue_db.insert_many(steps)

    def get_next_step(self):
        """
        Retrieve the next step in queue.
        """
        return self.step_queue_db.find_one()

    def get_queue_count(self):
        """
        Retrieve the number of steps in the queue.

        Returns:
            int: number of steps in the queue.
        """
        return self.step_queue_db.count()

    def remove_step(self, step_num):
        """
        Remove a step from the queue.

        Args:
            step_num (int): step number to remove from the queue.

        Returns:
            object: result of the delete operation.
        """
        return self.step_queue_db.delete_one({"step_num": step_num})

    def clear_queue(self):
        """
        Deletes everything in the queue.

        Returns:
            object: result of the delete operation.
        """
        return self.step_queue_db.delete_many({})
