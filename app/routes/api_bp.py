from flask import Blueprint
from ..controllers.apis.puzzle import *
from ..controllers.apis.auth import *
import pymongo

api_bp = Blueprint('api_bp', __name__)

# /api/puzzle
api_bp.route("/puzzle")(get_puzzles)

# /api/puzzle/<puzzle_id>
api_bp.route("/puzzle/<puzzle_id>")(get_puzzle_by_id)

# /api/puzzle/create
api_bp.route("/puzzle/create", methods=["POST"])(create_puzzle)

# /api/puzzle/update
api_bp.route("/puzzle/update", methods=["PUT"])(update_puzzle)

# /api/puzzle/delete/<puzzle_id>
api_bp.route("/puzzle/delete/<puzzle_id>", methods=["DELETE"])(delete_puzzle)

# /api/puzzle/solve
api_bp.route("/puzzle/solve", methods=["POST"])(solve_puzzle)

# /api/puzzle/step-through
api_bp.route("/puzzle/step-through", methods=["POST"])(step_through)
