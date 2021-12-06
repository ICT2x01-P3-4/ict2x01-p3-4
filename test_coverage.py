import unittest

from dotenv import load_dotenv
from app import get_app_with_config
from app.models.puzzle_model import PuzzleModel
from config import TestConfig

# Loading Test configuration, so it would not mess with main config
app, mongodb = get_app_with_config(TestConfig)

PUZZLE = PuzzleModel()
DATA = {'name': 'test',
        'difficulty': 5,
        'puzzle_flow': '0',
        'puzzle_steps': 'test'}


class test_puzzle_model(unittest.TestCase):
    def test_puzzle_data(self):
        # Puzzle did not exist
        self.assertEqual(PUZZLE.create_puzzle(DATA), True)
        # A reinsertion, when puzzle already exist
        self.assertEqual(PUZZLE.create_puzzle(DATA), False)

    def test_validate_puzzle(self):
        # True Conditions
        self.assertEqual(PUZZLE.validate_puzzle(DATA), True)

        # False Conditions
        # Invalid name
        data = {'name': '', 'difficulty': 5,
                'puzzle_steps': '', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

        # Invalid difficulty level
        data = {'name': 'test', 'difficulty': 0,
                'puzzle_steps': '', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

        # Invalid steps list length
        data = {'name': 'test', 'difficulty': 5,
                'puzzle_steps': '', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

        # Invalid Puzzle Flow list length
        data = {'name': 'test', 'difficulty': 5,
                'puzzle_steps': '1', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)


if __name__ == '__main__':
    load_dotenv()
    unittest.main()
