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

    def insert_to_queue(self, step):
        """
        Insert a step into the queue.

        Args:
            step (dict): step to insert into the queue.
        """
        self.queue.insert_one(step)

    def get_next_step(self):
        """
        Retrieve the next step in queue.
        """
        step = self.queue.find_one({})
        if not step:
            return None
        return step["direction"]

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

    def dequeue(self):
        """
        Retrieve the next step in queue.
        """
        if self.get_queue_count() >= 1:
            self.queue.find_one_and_delete({})

    def is_empty(self):
        """
        Check if queue is empty.

        Returns:
            boolean: True if queue is empty, False otherwise.
        """
        return self.queue.count() == 0
