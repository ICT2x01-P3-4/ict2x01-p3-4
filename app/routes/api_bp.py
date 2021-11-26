from flask import Blueprint
import app.apis.freestyle_api as freestyle_api
import app.apis.puzzle_api as puzzle_api
import app.apis.car_api as car_api

api_bp = Blueprint('api_bp', __name__)

# /api/puzzle
api_bp.route("/puzzle")(puzzle_api.get_puzzles)

# /api/puzzle/<puzzle_id>
api_bp.route("/puzzle/<puzzle_id>")(puzzle_api.get_puzzle_by_id)

# /api/puzzle/create
api_bp.route("/puzzle/create", methods=["POST"])(puzzle_api.create_puzzle)

# /api/puzzle/update/<puzzle_id>
api_bp.route("/puzzle/update/<puzzle_id>",
             methods=["PUT"])(puzzle_api.update_puzzle)

# /api/puzzle/delete/<puzzle_id>
api_bp.route("/puzzle/delete/<puzzle_id>",
             methods=["DELETE"])(puzzle_api.delete_puzzle)

# /api/puzzle/solve/<puzzle_id>
api_bp.route("/puzzle/solve/<puzzle_id>",
             methods=["POST"])(puzzle_api.solve_puzzle)

# /api/puzzle/step-through/<puzzle_id>
api_bp.route("/puzzle/step-through/<puzzle_id>",
             methods=["POST"])(puzzle_api.step_through)

# /api/freestyle/execute
api_bp.route("/freestyle/execute", methods=["POST"])(freestyle_api.execute)

# /api/car/command
api_bp.route("/car/command")(car_api.get_command)

# /api/car/start
api_bp.route("/car/start")(car_api.start_car)

# /api/car/stop
api_bp.route("/car/stop")(car_api.stop_car)

# /api/car/obstacle
api_bp.route("/car/obstacle")(car_api.detected_obstacle)

api_bp.route("/car/insert-queue", methods=["POST"])(car_api.insert_queue)
