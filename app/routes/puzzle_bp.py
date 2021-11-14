from flask import Blueprint
from ..controllers.puzzle_management import create_puzzle, delete_puzzle, find_puzzles, find_puzzle, update_puzzle
from ..controllers.puzzle import puzzle_mode, solve_puzzle, step_through

puzzle_bp = Blueprint('puzzle_bp', __name__)

# Puzzle management
puzzle_bp.route('/create', methods=['GET', 'POST'])(create_puzzle)
puzzle_bp.route('/', methods=['GET'])(find_puzzles)
puzzle_bp.route('/update', methods=['GET', 'PUT'])(update_puzzle)
puzzle_bp.route('/<puzzle_id>', methods=['GET'])(find_puzzle)
puzzle_bp.route('/<puzzle_id>', methods=['DELETE'])(delete_puzzle)

# Puzzle game mode
puzzle_bp.route('/game', methods=['GET'])(puzzle_mode)
puzzle_bp.route('/solve', methods=['POST'])(solve_puzzle)
puzzle_bp.route('/step', methods=['POST'])(step_through)
