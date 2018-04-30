from flask import jsonify, abort, make_response, request
from app import app, data_artists
from app.login import auth


@app.route('/music-archive/api/v1/artists', methods=['GET'])
@auth.login_required
def get_artists():
    return jsonify({'artists': data_artists})


@app.route('/music-archive/api/v1/artists/<int:artist_id>', methods=['GET'])
@auth.login_required
def get_artist(artist_id):
    artist = [artist for artist in data_artists if artist['id'] == artist_id]
    if len(artist) == 0:
        abort(404)
    return jsonify({'artist': artist[0]})


@app.route('/music-archive/api/v1/artists', methods=['POST'])
@auth.login_required
def create_artist():
    if not request.json or not 'name' in request.json:
        abort(400)
    artist = {
        'id': data_artists[-1]['id'] + 1,
        'name': request.json['name'],
        'genres': request.json.get('genres', ""),
        'born': request.json['born']
    }
    data_artists.append(artist)
    return jsonify({'artist': artist}), 201


@app.route('/music-archive/api/v1/artists/<int:artist_id>', methods=['DELETE'])
@auth.login_required
def delete_artist(artist_id):
    artist = [artist for artist in data_artists if artist['id'] == artist_id]
    if len(artist) == 0:
        abort(404)
    data_artists.remove(artist[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)
