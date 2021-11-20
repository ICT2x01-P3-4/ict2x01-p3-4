from flask import Blueprint
from ..apis.puzzle_api import *
from ..apis.car_api import *

api_bp = Blueprint('api_bp', __name__)

# /api/puzzle
api_bp.route("/puzzle")(get_puzzles)

# /api/puzzle/<puzzle_id>
api_bp.route("/puzzle/<puzzle_id>")(get_puzzle_by_id)

# /api/puzzle/create
api_bp.route("/puzzle/create", methods=["POST"])(create_puzzle)

# /api/puzzle/update/<puzzle_id>
api_bp.route("/puzzle/update/<puzzle_id>", methods=["PUT"])(update_puzzle)

# /api/puzzle/delete/<puzzle_id>
api_bp.route("/puzzle/delete/<puzzle_id>", methods=["DELETE"])(delete_puzzle)

# /api/puzzle/solve/<puzzle_id>
api_bp.route("/puzzle/solve/<puzzle_id>", methods=["POST"])(solve_puzzle)

# /api/puzzle/step-through/<puzzle_id>
api_bp.route("/puzzle/step-through/<puzzle_id>",
             methods=["POST"])(step_through)

# /api/car/command
api_bp.route("/car/command")(get_command)

# /api/car/start
api_bp.route("/car/start")(start_car)

# /api/car/stop
api_bp.route("/car/stop")(stop_car)

# /api/car/obstacle
api_bp.route("/car/obstacle")(detected_obstacle)
