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
