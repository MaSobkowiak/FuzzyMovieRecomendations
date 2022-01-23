from flask import Flask, render_template, Response, request, redirect, url_for
import logging.config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from os import path
from flask_cors import CORS
import pandas as pd


Base = declarative_base()
DB_NAME = "moviesdb.db"


def create_app():
    app = Flask(__name__)
    CORS(app)
    # app.config['SECRET_KEY'] = "hferuifhiuerifer"
    # app.config['SLQALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    create_db()

    return app


def create_db():
    # if not path.exists('web' + DB_NAME):
    #     db.create_all(app=app)
    #     print('Movie db created!')
    from .models import Movie

    url = f'sqlite:///{DB_NAME}'
    engine = create_engine(url, echo=True)

    #Base.metadata.create_all(engine)

    filename = 'src/movies.tsv'
    movie = pd.read_csv(filename, sep='\t')
    movie.to_sql('movies', con=engine, if_exists='replace', index=False, index_label='id')


def get_movies(year, budget, mood, duration, vote, popularity):
    # TU pobrać odpowiednie filmy z bazy
    from .models import Movie

    url = f'sqlite:///{DB_NAME}'

    engine = create_engine(url, echo=True)
    session = sessionmaker(bind=engine)
    s = session()
    res = s.query(Movie).limit(5).all()

    movies = []
    for r in res:
        movie = {}
        movie['id']=r.id
        movie['title']=r.title
        movie['duration']=r.runtime
        movie['description']=r.overview
        movie['country']=r.original_language
        movie['genre']=r.genres
        movie['score']=r.vote_average
        movie['accuracy']='99%'
        movie['poster']='https://image.tmdb.org/t/p/w500/'+r.poster_path
        
        movies.append(movie)

    # movies = [
    #     {
    #         "id": 'fdasfda',
    #         "title": 'Toy Story',
    #         "duration": 120,
    #         "description": "lorem ipsum bla bla bla",
    #         "country": 'US',
    #         "genre": 'Animation',
    #         "score": 7.5,
    #         "accuracy": 93.3,
    #         "poster": '',
    #     },
    #     {
    #         "id": 'fdasfda',
    #         "title": 'Toy Story',
    #         "duration": 120,
    #         "description": "lorem ipsum bla bla bla",
    #         "country": 'US',
    #         "genre": 'Animation',
    #         "score": 7.5,
    #         "accuracy": 93.3,
    #         "poster": 'https://image.tmdb.org/t/p/w500/jSozzzVOR2kfXgTUuGnbgG2yRFi.jpg?fbclid=IwAR0M63XT0IHaKr922wH_0Dmu5-SeVv02c-V9xK6TLEPVcAe7tr5uTPvrfSU',
    #     }
    # ]
    return movies
