from ..db import mongo


class Puzzle():
    def __init__(self, data=None):
        if data is not None:
            self.id = data["id"]
            self.name = data["name"]
            self.difficulty = data["difficulty"]
            self.puzzle_shape = data["puzzle_shape"]
            self.puzzle_steps = data["puzzle_steps"]
        self.db = mongo.db.puzzles

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
        result = self.db.insert_one({
            "id": puzzle.id,
            "name": puzzle.name,
            "difficulty": puzzle.difficulty,
            "puzzle_shape": puzzle.puzzle_shape,
            "puzzle_steps": puzzle.puzzle_steps
        })
        return result.inserted_id

    def get_all_puzzles(self):
        return list(self.db.find({}, {"_id": False}))

    def get_puzzle(self, id):
        return self.db.find_one({"id": id}, {"_id": False})

    def update_puzzle(self, puzzle):
        result = self.db.update_one({"id": puzzle.id}, {
            "$set": {
                "name": puzzle.name,
                "difficulty": puzzle.difficulty,
                "puzzle_shape": puzzle.puzzle_shape,
                "puzzle_steps": puzzle.puzzle_steps
            }
        })
        return result.matched_count

    def delete_puzzle(self, id):
        result = self.db.delete_one({"id": id})
        return result.deleted_count

    def generate_shape(self):
        # TODO: generate puzzle shape
        pass
