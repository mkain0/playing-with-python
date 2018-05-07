from flask import jsonify, abort, request, render_template
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app import db, app
from app.login import auth
from app.models import Url, Artist, ArtistSchema


@app.route('/music-archive/api/v1/')
@app.route('/music-archive/api/v1/index')
def index():
    data_endpoints = Url.query.all()
    return render_template('index.html', title='Music Archive API', endpoints=data_endpoints)


class ArtistsCollection(Resource):
    @auth.login_required
    def get(self):
        artist_schema = ArtistSchema(many=True)
        return jsonify({'artists': artist_schema.dump(Artist.query.all()).data})

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
        return jsonify({'artist': artist_schema.dump(artist).data})

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
        return jsonify({'artist': artist_schema.dump(artist).data})

    @auth.login_required
    def delete(self, id):
        artist = Artist.query.get(id)
        if artist is None:
            abort(404)
        db.session.delete(artist)
        db.session.commit()
        return jsonify({'result': True})
