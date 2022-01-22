from . import db


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    adult = db.Column(db.Boolean)
    budget = db.Column(db.BigInteger) #??
    genres = db.Column(db.String(2000))
    original_language = db.Column(db.String(100))
    overview = db.Column(db.String(5000))
    popularity = db.Column(db.Float)
    poster_path = db.Column(db.String(1000))
    release_date = db.Column(db.Date)
    runtime = db.Column(db.Float)
    vote_avg = db.Column(db.Float)
    vote_count = db.Column(db.Float)



class Credit(db.Model):
    __tablename__ = 'credits'
    id = db.Column(db.Integer, primary_key=True)
    cast = db.Column(db.String(5000))
    crew = db.Column(db.String(5000))
    movieId = db.Column(db.Integer, db.ForeignKey('movie.id'))


class Keyword(db.Model):
    __tablename__ = 'keywords'
    id = db.Column(db.Integer, primary_key=True)
    keywords = db.Column(db.String(5000))
    movieId = db.Column(db.Integer, db.ForeignKey('movie.id'))

class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    rating = db.Column(db.Float)
    movieId = db.Column(db.Integer, db.ForeignKey('movieId'))