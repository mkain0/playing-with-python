from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from passlib.hash import pbkdf2_sha256

from project.models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    return pbkdf2_sha256.verify(password, user.password)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
