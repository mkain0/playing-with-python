from app import db
from app.models import Url, User, Artist


def add(type, object, identifier):
    old_object = type.query.get(identifier)
    db.session.delete(old_object)
    db.session.commit()
    db.session.add(object)
    db.session.commit()


add(Url, Url(url='/music-archive/api/v1/artists', description='LIST artist'), '/music-archive/api/v1/artists')
add(User, User(id=1, username='admin', password='1234'), 1)
add(Artist, Artist(id=1, name='Dua Lipa', genres='Pop, R&B', born='22 August 1995'), 1)
add(Artist, Artist(id=2, name='Shirley Ann Manson', genres='Pop, Alternative rock', born='26 de agosto de 1966'), 2)
