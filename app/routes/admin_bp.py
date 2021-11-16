from flask import Blueprint
from ..controllers.admin import index

admin_bp = Blueprint('admin_bp', __name__)

# /admin
admin_bp.route("/")(index)

# /admin/profile
admin_bp.route("/profile")

# /admin/puzzle
admin_bp.route('/puzzle')

# /admin/puzzle/<puzzle_id>
admin_bp.route('/<puzzle_id>')

# /admin/puzzle/create
admin_bp.route('/create')
