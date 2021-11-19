from ..db import mongo
from .entities.puzzle_entity import Puzzle
from bson import ObjectId


class PuzzleModel:
    def __init__(self):
        self.puzzle_db = mongo.db.puzzles

    def create_puzzle(self, data):
        """
        Insert a new puzzle into the database.

        Args:
            puzzle (object): puzzle object to be inserted into the database.

        Returns:
            string: id of the newly inserted puzzle.
        """
        new_puzzle = Puzzle(data["name"], data["difficulty"],
                            data["puzzle_shape"], data["puzzle_steps"])
        inserted_id = self.puzzle_db.insert_one(
            new_puzzle.__dict__).inserted_id
        new_puzzle.set_id(str(inserted_id))
        new_puzzle._id = str(inserted_id)
        return new_puzzle

    def get_all_puzzles(self):
        """
        Return all puzzles in the database.

        Returns:
            list: all puzzles in the database.
        """
        return list(self.puzzle_db.find({}).sort("difficulty", 1))

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
