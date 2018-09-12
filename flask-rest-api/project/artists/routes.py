from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from werkzeug.exceptions import abort

from project import db
from project.login import auth
from project.models import ArtistSchema, Artist


class ArtistsCollection(Resource):
    @auth.login_required
    def get(self):
        artist_schema = ArtistSchema(many=True)
        return {'artists': artist_schema.dump(Artist.query.all()).data}

    @auth.login_required
    def post(self):
        self.validate_request()
        id = Artist.query.order_by(Artist.id.desc()).first().id + 1
        artist = Artist(id=id,
                        name=request.json['name'],
                        genres=request.json.get('genres', ""),
                        born=request.json['born'])
        db.session.add(artist)
        db.session.commit()
        artist_schema = ArtistSchema(many=False)
        return {'artist': artist_schema.dump(artist).data}, 201

    @staticmethod
    def validate_request():
        if not request.json:
            abort(400)
        request_parser = RequestParser(bundle_errors=True)
        request_parser.add_argument("name", required=True, help="name field is required.")
        request_parser.add_argument("born", required=True, help="born field is required.")
        arguments = request_parser.parse_args()
        if arguments:
            return arguments


class Artists(Resource):
    @auth.login_required
    def get(self, id):
        artist = Artist.query.get(id)
        if artist is None:
            abort(404)
        artist_schema = ArtistSchema(many=False)
        return {'artist': artist_schema.dump(artist).data}

    @auth.login_required
    def delete(self, id):
        artist = Artist.query.get(id)
        if artist is None:
            abort(404)
        db.session.delete(artist)
        db.session.commit()
        return {'result': True}
