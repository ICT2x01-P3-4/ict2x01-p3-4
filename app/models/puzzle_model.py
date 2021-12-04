from ..db import mongo
from .queue_model import QueueModel
from .entities.step_entity import Step
from .entities.puzzle_entity import Puzzle
from bson import ObjectId


class PuzzleModel:
    def __init__(self):
        self.puzzle_db = mongo.db.puzzles

    def create_puzzle(self, data):
        """
        Insert a new puzzle into the database.

        Args:
            puzzle (dict): puzzle object to be inserted into the database.

        Returns:
            string: id of the newly inserted puzzle.
        """
        new_puzzle = Puzzle(data["name"], data["difficulty"],
                            data["puzzle_steps"], data["puzzle_flow"])
        result = self.puzzle_db.insert_one(
            new_puzzle.__dict__)
        return str(result.inserted_id)

    def get_all_puzzles(self):
        """
        Return all puzzles in the database.

        Converts the _id object to string.

        Returns:
            list: all puzzles in the database sorted by difficulty level in ascending order.
        """
        puzzles = list(self.puzzle_db.find({}).sort("difficulty", 1))

        for puzzle in puzzles:
            puzzle["_id"] = str(puzzle["_id"])
        return puzzles

    def get_puzzles_count(self):
        """
        Counts number of puzzles in database.

        Returns:
            int: number of puzzles in database.
        """
        return self.puzzle_db.count_documents({})

    def get_puzzle(self, id):
        """
        Return a puzzle from the database.

        Args:
            id (string): id of the puzzle to be returned.

        Returns:
            object: puzzle object from the database.
        """
        puzzle = self.puzzle_db.find_one({"_id": ObjectId(id)})
        if puzzle:
            puzzle["_id"] = str(puzzle["_id"])
        return puzzle

    def get_puzzle_by_stage(self, stage):
        """
        Retrieve puzzle by stage difficulty

        Args:
            stage (int)): Stage number
        """
        return self.puzzle_db.find_one({"difficulty": stage})

    def update_puzzle(self, puzzle_id, puzzle):
        """
        Updates a puzzle in the database.

        Args:
            puzzle (object): puzzle object to be updated.

        Returns:
            int: number of puzzles updated.
        """
        puzzle = Puzzle(puzzle["name"], puzzle["difficulty"],
                        puzzle_shape=puzzle["puzzle_shape"], puzzle_steps=puzzle["puzzle_steps"])
        result = self.puzzle_db.update_one({"_id": ObjectId(puzzle_id)}, {
            "$set": puzzle.__dict__
        })
        return result.matched_count

    def delete_puzzle(self, id):
        """
        Delete a puzzle from the database.

        Args:
            id (string): id of the puzzle to be deleted.

        Returns:
            int: number of puzzles deleted.
        """
        result = self.puzzle_db.delete_one({"_id": ObjectId(id)})
        return result.deleted_count

    def solve_puzzle(self, puzzle_id, steps):
        """
        Solve a puzzle in the database.

        Args:
            puzzle_id (string): id of the puzzle to be solved.
            steps (list): steps to be executed.

        Returns:
            boolean: True if completed all execution. False if not.
        """
        puzzle = self.get_puzzle(puzzle_id)

        is_correct = self.check_answer(puzzle, steps, True)

        if not is_correct:
            return False

        # Format steps into list of dicts
        steps_arr = []
        for i, step in enumerate(steps):
            step_obj = Step(i+1, step)
            steps_arr.append(step_obj.__dict__)

        # Insert steps into queue
        queue_model = QueueModel()
        queue_model.create_queue(steps_arr)

        return True

    def step_through_puzzle(self, puzzle_id, step):
        """
        Checks for user's answer and executes step.

        Args:
            puzzle_id (string): id of the puzzle to be solved.
            step (dict): step to be executed.

        Returns:
            boolean: True if completed execution, False if not.
        """
        puzzle = self.get_puzzle(puzzle_id)
        is_correct = self.check_answer(puzzle, step, False)

        if not is_correct:
            return False

        queue = QueueModel()
        queue.create_queue([step])
        return True

    def check_answer(self, puzzle, steps, is_solve):
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

    def execute_steps(self, steps):
        """
        Inserts steps into queue in db
        and wait for it to be emptied.

        Args:
            steps (list): list of steps.
        """
        # Format steps into list of dicts
        steps_arr = []
        for i, step in enumerate(steps):
            step_obj = Step(i+1, step)
            steps_arr.append(step_obj.__dict__)

        # Insert steps into queue
        queue = QueueModel()
        queue.create_queue(steps_arr)

        # Wait for queue to be emptied
        while True:
            if queue.is_empty():
                break

    def at_last_step(self, puzzle_id, step):
        """
        Checks if user is at last step of puzzle.

        Args:
            puzzle_id (string): id of puzzle.
            step (object): step object.

        Returns:
            boolean: True if current steps is last step of puzzle.
        """
        puzzle = self.get_puzzle(puzzle_id)
        total_steps = len(puzzle["puzzle_steps"])
        return step["step_num"] == total_steps
