from flask import make_response, jsonify

from app import app


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def not_found():
    return make_response(jsonify({'error': 'Internal server error'}), 500)
