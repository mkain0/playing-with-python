from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    with app.app_context():
        initialize_api_resource(app)
        initialize_extensions(app)
        initialize_database()
        register_blueprints(app)
    return app


def initialize_api_resource(app):
    from project.artists.routes import Artists
    from project.artists.routes import ArtistsCollection
    api = Api(app, prefix="/music-archive/api/v1")
    api.add_resource(ArtistsCollection, '/artists')
    api.add_resource(Artists, '/artists', '/artists/<int:id>')


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)


def initialize_database():
    from project.data import init_database
    init_database()


def register_blueprints(app):
    from project.users import users_blueprint
    from project.artists import artists_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(artists_blueprint)
