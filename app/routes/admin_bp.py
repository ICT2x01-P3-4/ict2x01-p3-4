from flask import Blueprint
from ..controllers.admin_controller import index, logout, profile, puzzle, edit_puzzle, create_puzzle, login

admin_bp = Blueprint('admin_bp', __name__)

# /admin
admin_bp.route("/")(index)

# /admin/profile
admin_bp.route("/profile")(profile)

# /admin/puzzle
admin_bp.route('/puzzle')(puzzle)

# /admin/puzzle/<puzzle_id>
admin_bp.route('/<puzzle_id>')(edit_puzzle)

# /admin/puzzle/create
admin_bp.route('/create')(create_puzzle)

# /admin/login
admin_bp.route('/login', methods=["POST"])(login)

# /admin/logout
admin_bp.route('/logout')(logout)
