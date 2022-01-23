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
from .models import *



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

        #Base.metadata.create_all(engine)

        filename = 'src/movies.tsv'
        movie = pd.read_csv(filename, sep='\t')
        movie.to_sql('movies', con=engine, if_exists='replace', index=False, index_label='id')
        print('Movie db created!')


def get_movies(year, budget, mood, duration, vote, popularity):
    # TU pobrać odpowiednie filmy z bazy


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

    return movies
