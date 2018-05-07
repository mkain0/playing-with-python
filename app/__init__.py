from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, prefix="/music-archive/api/v1")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

marshmallow = Marshmallow(app)

from app import login, routes, models, data
from app.routes import Artists, ArtistsCollection

api.add_resource(ArtistsCollection, '/artists')
api.add_resource(Artists, '/artists/<int:id>')

if __name__ == '__main__':
    app.run(debug=False)
