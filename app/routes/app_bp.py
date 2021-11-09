from flask import Blueprint
from ..controllers.app_controller import index

app_bp = Blueprint('app_bp', __name__)

app_bp.route('/') (index)