"""Blueprints for api routes"""
from flask import Blueprint

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/')
def index():
    return 'API Running...'