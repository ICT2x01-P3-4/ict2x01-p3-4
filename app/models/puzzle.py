from ..db import mongo
from bson import ObjectId


class Puzzle():
    def __init__(self, puzzle=None):
        if puzzle is not None:
            self.id = puzzle["id"] if "id" in puzzle else ""
            self.name = puzzle["name"]
            self.difficulty = puzzle["difficulty"]
            self.puzzle_shape = puzzle["puzzle_shape"]
            self.puzzle_steps = puzzle["puzzle_steps"]
        self.puzzle_db = mongo.db.puzzles

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_puzzle_shape(self):
        return self.puzzle_shape

    def set_puzzle_shape(self, puzzle_shape):
        self.puzzle_shape = puzzle_shape

    def get_puzzle_steps(self):
        return self.puzzle_steps

    def set_puzzle_steps(self, puzzle_steps):
        self.puzzle_steps = puzzle_steps

    def create_puzzle(self, puzzle):
        """
        Insert a new puzzle into the database.

        Args:
            puzzle (object): puzzle object to be inserted into the database.

        Returns:
            string: id of the newly inserted puzzle.
        """
        result = self.puzzle_db.insert_one({
            "name": puzzle.name,
            "difficulty": puzzle.difficulty,
            "puzzle_shape": puzzle.puzzle_shape,
            "puzzle_steps": puzzle.puzzle_steps
        })
        return result.inserted_id

    def get_all_puzzles(self):
        """
        Return all puzzles in the database.

        Returns:
            list: all puzzles in the database.
        """
        return list(self.puzzle_db.find({}))

    def get_puzzle(self, id):
        """
        Return a puzzle from the database.

        Args:
            id (string): id of the puzzle to be returned.

        Returns:
            object: puzzle object from the database.
        """
        return self.puzzle_db.find_one({"_id": ObjectId(id)})

    def update_puzzle(self, puzzle):
        """
        Updates a puzzle in the database.

        Args:
            puzzle (object): puzzle object to be updated.

        Returns:
            int: number of puzzles updated.
        """
        result = self.puzzle_db.update_one({"_id": ObjectId(puzzle.id)}, {
            "$set": {
                "name": puzzle.name,
                "difficulty": puzzle.difficulty,
                "puzzle_shape": puzzle.puzzle_shape,
                "puzzle_steps": puzzle.puzzle_steps
            }
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

    def generate_shape(self):
        # TODO: generate puzzle shape
        pass
