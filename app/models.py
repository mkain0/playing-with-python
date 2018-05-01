from app import db, marshmallow


class Url(db.Model):
    url = db.Column(db.String(140), primary_key=True)
    description = db.Column(db.String(140))

    def __repr__(self):
        return '<Url {}>'.format(self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), index=True)
    genres = db.Column(db.String(140))
    born = db.Column(db.String(140))

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class UserSchema(marshmallow.ModelSchema):
    class Meta:
        model = User


class ArtistSchema(marshmallow.ModelSchema):
    class Meta:
        model = Artist
