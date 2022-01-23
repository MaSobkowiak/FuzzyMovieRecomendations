from sqlalchemy import Column, Integer, String, Float, BigInteger, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    # __table_args__ = {"schema":"moviesdb"}
    id = Column(Integer, primary_key=True)
    title = Column(String(1000))
    adult = Column(Boolean)
    budget = Column(BigInteger) #??
    genres = Column(String(2000))
    original_language = Column(String(100))
    overview = Column(String(5000))
    popularity = Column(Float)
    poster_path = Column(String(1000))
    release_date = Column(Date)
    runtime = Column(Float)
    vote_average = Column(Float)
    vote_count = Column(Float)



# class Rating(db.Model):
#     __tablename__ = 'ratings'
#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer)
#     rating = db.Column(db.Float)
#     movieId = db.Column(db.Integer, db.ForeignKey('movieId'))