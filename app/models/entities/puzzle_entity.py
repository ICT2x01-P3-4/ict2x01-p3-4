class Puzzle:
    def __init__(self, name, difficulty, puzzle_shape, puzzle_steps,  id="",):
        self.id = id
        self.name = name
        self.difficulty = difficulty
        self.puzzle_shape = puzzle_shape
        self.puzzle_steps = puzzle_steps

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
