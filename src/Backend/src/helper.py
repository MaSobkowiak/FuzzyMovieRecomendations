from flask import Flask, render_template, Response, request, redirect, url_for
import logging.config
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from os import path
from flask_cors import CORS
import pandas as pd
from .models import *
from .fuzzy import get_fuzzy
import requests


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
    if path.exists(DB_NAME):
        print('Database already exists...')
    else:

        url = f'sqlite:///{DB_NAME}'
        engine = create_engine(url, echo=True)

        # Base.metadata.create_all(engine)

        filename = 'src/movies.tsv'
        movie = pd.read_csv(filename, sep='\t')
        movie.to_sql('movies', con=engine, if_exists='replace',
                     index=False, index_label='id')
        print('Movie db created!')


def get_semantic(val):
    if(val == "0"):
        return "low"
    elif(val == "1"):
        return "medium"
    elif(val == "2"):
        return "high"


def check_poster(poster_path):
    url = "https://image.tmdb.org/t/p/w500/" + poster_path
    # status_code = urllib.request.urlopen(url).getcode()
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return url
    except requests.exceptions.HTTPError as err:
        return ''


def check_genre(genre):
    if(genre):
        return str(json.loads(genre.replace("'", "\""))[0]['name'])
    else:
        return 'No data'


def get_movies(year, budget, mood, duration, vote, popularity):
    # TU pobrać odpowiednie filmy z bazy

    url = f'sqlite:///{DB_NAME}'

    engine = create_engine(url, echo=True)
    session = sessionmaker(bind=engine)
    s = session()
    res = s.query(Movie).all()

    movies = []
    for m in res:
        comp = get_fuzzy(year, budget, mood, duration, vote, popularity, m)
        if(min(comp) > 0.5):
            movie = {}
            movie['id'] = m.id
            movie['title'] = m.title
            movie['poster'] = check_poster(m.poster_path)
            movie['country'] = m.original_language
            movie['accuracy'] = '99'
            movie['description'] = m.overview

            movie['year'] = m.release_date
            movie['budget'] = m.budget
            movie['genre'] = check_genre(m.genres)
            movie['duration'] = m.runtime
            movie['score'] = m.vote_average
            movie['popularity'] = m.popularity

            movies.append(movie)

        if(len(movies) > 10):
            break

    return movies
