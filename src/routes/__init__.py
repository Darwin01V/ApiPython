from flask import Blueprint
from src.routes.user import bp as user_bp

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Registra los Blueprints individuales
api_bp.register_blueprint(user_bp)
