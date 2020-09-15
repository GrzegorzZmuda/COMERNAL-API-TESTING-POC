from flask import jsonify
from flask import Blueprint

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(404)
def not_found(error):
    return  jsonify({"error": "not found"}), 404

@bp.app_errorhandler(500)
def server_error(error):
    return  jsonify({"error": "server error"}), 500