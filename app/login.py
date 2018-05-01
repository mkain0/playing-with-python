from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from app.models import User

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    users = User.query.all()
    for user in users:
        if user.username == username:
            return user.password
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
