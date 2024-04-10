from flask import Blueprint, jsonify

# Create a blueprint for error handling routes
errors = Blueprint('errors', __name__)

# Route to handle 404 errors (Not Found)
@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

# Route to handle 500 errors (Internal Server Error)
@errors.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500
