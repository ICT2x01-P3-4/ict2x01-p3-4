from flask import Blueprint
import app.apis.freestyle_api as freestyle_api
import app.apis.puzzle_api as puzzle_api
import app.apis.car_api as car_api
import app.apis.admin_api as admin_api

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

# /api/puzzle/check-queue
api_bp.route("/puzzle/check-queue")(puzzle_api.check_puzzle_queue)

# /api/puzzle/update-score
api_bp.route("/puzzle/update-score", methods=["POST"])(puzzle_api.update_score)

# /api/puzzle/total
api_bp.route("/puzzle/total")(puzzle_api.get_total_puzzles)

# /api/freestyle/execute
api_bp.route("/freestyle/execute", methods=["POST"])(freestyle_api.execute)

# /api/freestyle/check-queue
api_bp.route("/freestyle/check-queue",
             methods=["GET"])(freestyle_api.check_queue)

# /api/car/command
api_bp.route("/car/command")(car_api.get_command)

# /api/car/start
api_bp.route("/car/start")(car_api.start_car)

# /api/car/stop
api_bp.route("/car/stop")(car_api.stop_car)

# /api/car/obstacle
api_bp.route("/car/obstacle")(car_api.detected_obstacle)

# /api/car/insert-queue
api_bp.route("/car/insert-queue", methods=["POST"])(car_api.insert_queue)

# /api/admin/create-user
api_bp.route("/admin/create-user", methods=["POST"])(admin_api.create_user)

# /api/admin/update-user
api_bp.route("/admin/update-user", methods=["PUT"])(admin_api.edit_user)

# /api/admin/delete-user
api_bp.route("/admin/delete-user", methods=["DELETE"])(admin_api.delete_user)

# /api/admin/change-password
api_bp.route("/admin/change-password",
             methods=["POST"])(admin_api.change_admin_password)
