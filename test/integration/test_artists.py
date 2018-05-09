import json

from pip._vendor import chardet

from test.integration.commons import load_json


def test_get_artist(app, authorization_header):
    response = app.get('/music-archive/api/v1/artists/1', headers=authorization_header, follow_redirects=True)
    json_data = json.loads(response.data.decode(chardet.detect(response.data)["encoding"]))
    expected_json = load_json('single_artist.json')

    assert response.status_code == 200
    assert json_data == expected_json


def test_delete_artist(app, authorization_header):
    response = app.delete('/music-archive/api/v1/artists/1', headers=authorization_header, follow_redirects=True)

    assert response.status_code == 200
