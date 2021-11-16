"""Blueprints for app views.

Do the following to add a new blueprint:
1. Import controllers.
2. Add the routes to app_bp.
3. Insert controller into the app router.
"""

from flask import Blueprint
from ..controllers.app_controller import index, userhome

app_bp = Blueprint('app_bp', __name__)

app_bp.route('/')(index)
app_bp.route('/userhome.html')(userhome)
