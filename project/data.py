from passlib.handlers.pbkdf2 import pbkdf2_sha256

from project import db
from project.models import Url, User, Artist


def add(object):
    db.session.add(object)
    db.session.commit()


def init_database():
    db.drop_all()
    db.create_all()

    add(Url(url='/music-archive/api/v1/artists', description='LIST artist'))
    add(User(id=1, username='admin', password=pbkdf2_sha256.hash('1234')))
    add(Artist(id=1, name='Dua Lipa', genres='Pop, R&B', born='22 August 1995'))
    add(Artist(id=2, name='Shirley Ann Manson', genres='Alternative rock', born='26 de agosto de 1966'))
