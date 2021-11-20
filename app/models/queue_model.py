from ..db import mongo


class QueueModel:
    def __init__(self):
        self.queue = mongo.db.queue

    def create_queue(self, steps):
        """
        Insert a list of steps into the queue.

        Args:
            steps (list): list of steps to insert into the queue.
        """
        self.queue.insert_many(steps)

    def get_next_step(self):
        """
        Retrieve the next step in queue.
        """
        step = self.queue.find_one()
        return step["direction"]

    def get_queue_count(self):
        """
        Retrieve the number of steps in the queue.

        Returns:
            int: number of steps in the queue.
        """
        return self.queue.count()

    def remove_step(self, step_num):
        """
        Remove a step from the queue.

        Args:
            step_num (int): step number to remove from the queue.

        Returns:
            object: result of the delete operation.
        """
        return self.queue.delete_one({"step_num": step_num})

    def clear_queue(self):
        """
        Deletes everything in the queue.

        Returns:
            object: result of the delete operation.
        """
        return self.queue.delete_many({})
