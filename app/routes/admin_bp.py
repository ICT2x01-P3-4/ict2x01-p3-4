from flask import Blueprint
from ..controllers.admin_controller import *

admin_bp = Blueprint('admin_bp', __name__)

# /admin/login
admin_bp.route("/login")(login)

# /admin
admin_bp.route("/")(index)

# /admin/profile
admin_bp.route("/profile")(profile)

# /admin/puzzle
admin_bp.route('/puzzle')(puzzle)

# /admin/puzzle/<puzzle_id>
admin_bp.route('/<puzzle_id>')(edit_puzzle)

# /admin/puzzle/<puzzle_id>
admin_bp.route('/view')(view_puzzle)

# /admin/puzzle/create
admin_bp.route('/create')(create_puzzle)

# /admin/login
admin_bp.route('/login',  methods=["GET", "POST"])(login)


# /admin/logout
admin_bp.route('/logout')(logout)
