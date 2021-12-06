import unittest

from dotenv import load_dotenv
from app import get_app_with_config
from app.models.puzzle_model import PuzzleModel
from config import TestConfig
from bson import ObjectId

# Loading Test configuration, so it would not mess with main config
app, mongodb = get_app_with_config(TestConfig)

PUZZLE = PuzzleModel()
DATA = {'name': 'test',
        'difficulty': 5,
        'puzzle_flow': '0',
        'puzzle_steps': 'test'}
ALL_DATA = [{'_id': '61ac6f4b43e8dcd637294a75', 'name': 'Simple Puzzle', 'difficulty': 1, 'puzzle_steps': ['F'], 'puzzle_flow': ['38', '31']}, {'_id': '61a5231b5100a6f340360af7', 'name': 'Medium Puzzle', 'difficulty': 2, 'puzzle_shape': [[0, 1, 0]],
                                                                                                                                                'puzzle_steps': ['F', 'R', 'F', 'F'], 'puzzle_flow': ['31', '24', '25', '18']}, {'_id': '61acc83913486876d6f20f36', 'name': 'old puzzle', 'difficulty': 4, 'puzzle_steps': ['F', 'R', 'F', 'F', 'F', 'F'], 'puzzle_flow': ['38', '31', '32', '33', '34', '35']}]


class test_puzzle_model(unittest.TestCase):
    def test_get_all_puzzles(self):
        self.assertEqual(PUZZLE.get_all_puzzles(), ALL_DATA)

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

    def test_get_puzzles_count(self):
        self.assertEqual(PUZZLE.get_puzzles_count(), 3)

    def test_get_puzzle(self):
        _id = '61ac6f4b43e8dcd637294a75'
        data = {'_id': '61ac6f4b43e8dcd637294a75', 'name': 'Simple Puzzle',
                'difficulty': 1, 'puzzle_steps': ['F'], 'puzzle_flow': ['38', '31']}
        self.assertEqual(PUZZLE.get_puzzle(_id), data)

    def test_get_puzzle_by_stage(self):
        data = {'_id': ObjectId('61ac6f4b43e8dcd637294a75'), 'name': 'Simple Puzzle',
                'difficulty': 1, 'puzzle_steps': ['F'], 'puzzle_flow': ['38', '31']}
        self.assertEqual(PUZZLE.get_puzzle_by_stage(1), data)


if __name__ == '__main__':
    load_dotenv()
    unittest.main()
