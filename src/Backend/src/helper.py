from flask import Flask, render_template, Response, request, redirect, url_for
import logging.config
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.sql.expression import func
from os import path
from flask_cors import CORS
from .fuzzy_vals import COMPOUNDS, COMPOUNDS_WITH_BUDGET
import pandas as pd
from .models import *
from .fuzzy import get_fuzzy
import requests
from bs4 import BeautifulSoup


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


def check_poster(poster_path, movie_title):
    url = "https://image.tmdb.org/t/p/w500/" + poster_path
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return url
    except requests.exceptions.HTTPError as err:

        try:
            header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                      "X-Requested-With": "XMLHttpRequest"}
            url = 'https://www.themoviedb.org/search?language=pl&query=' + \
                movie_title.replace(" ", "+").lower()

            page = requests.get(url, headers=header).text

            soup = BeautifulSoup(page, 'html.parser')

            for raw_img in soup.find_all('img', {"class": "poster"}):
                link = raw_img.get('src')
                if link:
                    return 'https://image.tmdb.org/t/p/w500/' + link
        except:
            return ''


def check_genre(genre):
    if(len(json.loads(genre.replace("'", "\""))) != 0):
        return str(json.loads(genre.replace("'", "\""))[0]['name'])
    else:
        return 'No data'


def check_budget(budget):
    if(budget == 0):
        return 'No data'
    else:
        return str(budget) + " $"


def check_weight(comp):
    # If budget == 0
    if(len(comp) == 4):
        return comp[0] * COMPOUNDS['RELEASE'] + comp[1] * COMPOUNDS['RUNTIME'] + comp[2] * COMPOUNDS['VOTE'] + comp[3] * COMPOUNDS['POPULARITY']
    if(len(comp) == 5):
        return comp[0] * COMPOUNDS_WITH_BUDGET['RELEASE'] + comp[1] * COMPOUNDS_WITH_BUDGET['RUNTIME'] + comp[2] * COMPOUNDS_WITH_BUDGET['VOTE'] + comp[3] * COMPOUNDS_WITH_BUDGET['POPULARITY'] + comp[4] * COMPOUNDS_WITH_BUDGET['BUDGET']


def get_movies(year, budget, mood, duration, vote, popularity):
    # TU pobrać odpowiednie filmy z bazy

    url = f'sqlite:///{DB_NAME}'

    engine = create_engine(url, echo=True)
    session = sessionmaker(bind=engine)
    s = session()
    res = s.query(Movie).order_by(func.random()).all()

    movies = []
    for m in res:
        comp = get_fuzzy(year, budget, mood, duration, vote, popularity, m)
        accuracy = check_weight(comp)
        if(accuracy > 0.7):
            movie = {}
            movie['id'] = m.id
            movie['title'] = m.title
            movie['poster'] = check_poster(m.poster_path, m.title)
            movie['country'] = m.original_language
            movie['accuracy'] = round(accuracy * 100, 2)
            movie['description'] = m.overview

            movie['year'] = str(m.release_date)
            movie['budget'] = check_budget(m.budget)
            movie['genre'] = check_genre(m.genres)
            movie['duration'] = m.runtime
            movie['score'] = m.vote_average
            movie['popularity'] = round(m.popularity, 1)

            movies.append(movie)
            print(comp, movie['title'])

        if(len(movies) > 8):
            break

    return sorted(movies, key=lambda d: d['accuracy'])
