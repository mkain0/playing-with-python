from flask import render_template

from project.models import Url
from project.users import users_blueprint


@users_blueprint.route('/music-archive/api/v1/')
@users_blueprint.route('/music-archive/api/v1/index')
def index():
    data_endpoints = Url.query.all()
    return render_template('index.html', title='Music Archive API', endpoints=data_endpoints)
