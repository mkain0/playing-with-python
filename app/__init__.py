from flask import Flask

app = Flask(__name__)

data_artists = [
    {
        'id': 1,
        'name': u'Dua Lipa',
        'genres': u'Pop, R&B',
        'born': u'22 August 1995'
    },
    {
        'id': 2,
        'name': u'Shirley Ann Manson',
        'genres': u'Pop, Alternative rock',
        'born': u'26 de agosto de 1966'
    }
]

from app import login, routes
