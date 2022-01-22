from flask import render_template, request
from . import db


@app.route('/', methods=['GET'])
def index():
    return "index"