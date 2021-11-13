from flask import Blueprint
from ..controllers.puzzle_management import create_puzzle, delete_puzzle, find_puzzles, find_puzzle, update_puzzle
from ..controllers.puzzle import solve_puzzle

puzzle_bp = Blueprint('puzzle_bp', __name__)

puzzle_bp.route('/create', methods=['POST'])(create_puzzle)
puzzle_bp.route('/', methods=['GET'])(find_puzzles)
puzzle_bp.route('/', methods=['PUT'])(update_puzzle)
puzzle_bp.route('/<puzzle_id>', methods=['GET'])(find_puzzle)
puzzle_bp.route('/<puzzle_id>', methods=['DELETE'])(delete_puzzle)

puzzle_bp.route('/solve', methods=['POST'])(solve_puzzle)
