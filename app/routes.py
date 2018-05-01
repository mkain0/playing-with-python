from flask import jsonify, abort, make_response, request, render_template
from app import app, db
from app.login import auth
from app.models import Url, Artist, ArtistSchema


@app.route('/music-archive/api/v1/')
@app.route('/music-archive/api/v1/index')
def index():
    data_endpoints = Url.query.all()
    return render_template('index.html', title='Music Archive API', endpoints=data_endpoints)


@app.route('/music-archive/api/v1/artists', methods=['GET'])
@auth.login_required
def get_artists():
    artist_schema = ArtistSchema(many=True)
    return jsonify({'artists': artist_schema.dump(Artist.query.all()).data})


@app.route('/music-archive/api/v1/artists/<int:artist_id>', methods=['GET'])
@auth.login_required
def get_artist(artist_id):
    artist = Artist.query.get(artist_id)
    if artist is None:
        abort(404)
    artist_schema = ArtistSchema(many=False)
    return jsonify({'artist': artist_schema.dump(artist).data})


@app.route('/music-archive/api/v1/artists', methods=['POST'])
@auth.login_required
def create_artist():
    if not request.json or not 'name' in request.json:
        abort(400)
    id = Artist.query.order_by(Artist.id.desc()).first().id + 1
    artist = Artist(id=id, name=request.json['name'], genres=request.json.get('genres', ""), born=request.json['born'])
    db.session.add(artist)
    db.session.commit()
    artist_schema = ArtistSchema(many=False)
    return jsonify({'artist': artist_schema.dump(artist).data}), 201


@app.route('/music-archive/api/v1/artists/<int:artist_id>', methods=['DELETE'])
@auth.login_required
def delete_artist(artist_id):
    artist = Artist.query.get(artist_id)
    if artist is None:
        abort(404)
    db.session.delete(artist)
    db.session.commit()
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)
