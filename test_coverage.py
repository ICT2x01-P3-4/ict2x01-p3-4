import unittest

from dotenv import load_dotenv
from app import get_app_with_config
from app.models.puzzle_model import PuzzleModel
from app.models.queue_model import QueueModel
from config import TestConfig
from bson import ObjectId

# Loading Test configuration, so it would not mess with main config
app, mongodb = get_app_with_config(TestConfig)

PUZZLE = PuzzleModel()
QUEUE = QueueModel()
TEST_DATA = {'name': 'test',
             'difficulty': 5,
             'puzzle_flow': '0',
             'puzzle_steps': 'test'}
ALL_DATA = [{'_id': '61ac6f4b43e8dcd637294a75', 'name': 'Simple Puzzle', 'difficulty': 1, 'puzzle_steps': ['F'], 'puzzle_flow': [38, 31]}, {'_id': '61a5231b5100a6f340360af7', 'name': 'Medium Puzzle', 'difficulty': 2, 'puzzle_shape': [[0, 1, 0]], 'puzzle_steps': ['F', 'F'], 'puzzle_flow': [31, 24, 17]}, {
    '_id': '61adbd45defed91778187579', 'name': 'Level 3 Puzzle', 'difficulty': 3, 'puzzle_steps': ['F', 'F', 'L', 'F'], 'puzzle_flow': [46, 39, 32, 31]}, {'_id': '61acc83913486876d6f20f36', 'name': 'old puzzle', 'difficulty': 4, 'puzzle_steps': ['F', 'R', 'F', 'F', 'F', 'F'], 'puzzle_flow': [38, 31, 32, 33, 34, 35]}]
DATA = {'_id': '61ac6f4b43e8dcd637294a75', 'name': 'Simple Puzzle',
        'difficulty': 1, 'puzzle_steps': ['F'], 'puzzle_flow': [38, 31]}


class test_puzzle_model(unittest.TestCase):
    def test_get_all_puzzles(self):
        self.assertEqual(PUZZLE.get_all_puzzles(), ALL_DATA)

    def test_create_puzzle(self):
        # Puzzle did not exist
        self.assertEqual(PUZZLE.create_puzzle(TEST_DATA), True)

        # A reinsertion, when puzzle already exist
        self.assertEqual(PUZZLE.create_puzzle(TEST_DATA), False)

        # Delete the test data for consistent data
        PUZZLE.puzzle_db.delete_one({'name': 'test'})

    def test_validate_puzzle(self):
        # True Conditions
        self.assertEqual(PUZZLE.validate_puzzle(DATA), True)

        # Invalid name triggering False Condition
        data = {'name': '', 'difficulty': 5,
                'puzzle_steps': '', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

        # Invalid difficulty level triggering False Condition
        data = {'name': 'test', 'difficulty': 0,
                'puzzle_steps': '', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

        # Invalid steps list length triggering False Condition
        data = {'name': 'test', 'difficulty': 5,
                'puzzle_steps': '', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

        # Invalid Puzzle Flow list length triggering False Condition
        data = {'name': 'test', 'difficulty': 5,
                'puzzle_steps': '1', 'puzzle_flow': ''}
        self.assertEqual(PUZZLE.validate_puzzle(data), False)

    def test_get_puzzles_count(self):
        self.assertEqual(PUZZLE.get_puzzles_count(), 4)

    def test_get_puzzle(self):
        self.assertEqual(PUZZLE.get_puzzle(DATA['_id']), DATA)

    def test_get_puzzle_by_stage(self):
        data = {'_id': ObjectId('61ac6f4b43e8dcd637294a75'), 'name': 'Simple Puzzle',
                'difficulty': 1, 'puzzle_steps': ['F'], 'puzzle_flow': [38, 31]}
        self.assertEqual(PUZZLE.get_puzzle_by_stage(1), data)

    def test_update_puzzle(self):
        # True Condition
        self.assertEqual(PUZZLE.update_puzzle(DATA['_id'], TEST_DATA), True)

        # Data already existed, trigger False condition
        self.assertEqual(PUZZLE.update_puzzle(DATA['_id'], TEST_DATA), False)

        # Reassign back the original values for data consistency
        PUZZLE.update_puzzle(DATA['_id'], DATA)

    def test_delete_puzzle(self):
        # Insert test data
        PUZZLE.puzzle_db.insert_one(TEST_DATA)
        pid = list(PUZZLE.puzzle_db.find({'name': 'test'}))[0]['_id']

        # Test delete
        self.assertEqual(PUZZLE.delete_puzzle(pid), 1)

    def test_solve_puzzle(self):
        # Wrong step to trigger False Condition
        wrong_step = ['L']
        self.assertEqual(PUZZLE.solve_puzzle(DATA['_id'], wrong_step), False)

        # True Condition
        self.assertEqual(PUZZLE.solve_puzzle(
            DATA['_id'], DATA['puzzle_steps']), True)

        # Clear Queue
        QUEUE.queue.delete_one({'direction': DATA['puzzle_steps'][0]})


if __name__ == '__main__':
    load_dotenv()
    unittest.main()
