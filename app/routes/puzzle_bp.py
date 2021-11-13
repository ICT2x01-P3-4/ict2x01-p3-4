from flask import Blueprint
from ..controllers.puzzle import index

puzzle_bp = Blueprint('puzzle_bp', __name__)

puzzle_bp.route('/')(index)
