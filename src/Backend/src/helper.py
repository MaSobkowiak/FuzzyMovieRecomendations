from flask import Flask, render_template, Response, request, redirect, url_for
import logging.config
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_cors import CORS


db = SQLAlchemy()
DB_NAME = "moviesdb.db"


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = "hferuifhiuerifer"
    app.config['SLQALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    create_db(app)

    return app


def create_db(app):
    if not path.exists('web' + DB_NAME):
        db.create_all(app=app)
        print('Movie db created!')


def get_movies(year, budget, mood, duration, vote, popularity):
    # TU pobrać odpowiednie filmy z bazy
    movies = [
        {
            "id": 'fdasfda',
            "title": 'Toy Story',
            "duration": 120,
            "description": "lorem ipsum bla bla bla",
            "country": 'US',
            "genre": 'Animation',
            "score": 7.5,
            "accuracy": 93.3,
            "poster": 'https://image.tmdb.org/t/p/w500/jSozzzVOR2kfXgTUuGnbgG2yRFi.jpg?fbclid=IwAR0M63XT0IHaKr922wH_0Dmu5-SeVv02c-V9xK6TLEPVcAe7tr5uTPvrfSU',
        },
        {
            "id": 'fdasfda',
            "title": 'Toy Story',
            "duration": 120,
            "description": "lorem ipsum bla bla bla",
            "country": 'US',
            "genre": 'Animation',
            "score": 7.5,
            "accuracy": 93.3,
            "poster": 'https://image.tmdb.org/t/p/w500/jSozzzVOR2kfXgTUuGnbgG2yRFi.jpg?fbclid=IwAR0M63XT0IHaKr922wH_0Dmu5-SeVv02c-V9xK6TLEPVcAe7tr5uTPvrfSU',
        }
    ]
    return movies
