from flask import Blueprint

artists_blueprint = Blueprint('artists', __name__)

from . import routes
