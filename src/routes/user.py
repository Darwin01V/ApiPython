from flask import Blueprint, jsonify, request
from src.Controller.UserController import get_usuarios, get_usuario

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def users_list():
    data = get_usuarios()
    return jsonify(data)

@bp.route('user/<string:usuario>', methods=['GET'])
def user_detail(usuario):
    data = get_usuario(usuario)
    return jsonify(data)
    
