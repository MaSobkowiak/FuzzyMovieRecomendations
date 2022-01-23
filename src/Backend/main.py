from src.helper import create_app, get_movies
import flask
from flask import request

app = create_app()


@app.route("/movies", methods=['GET'])
def movies():
    year = request.args.get('year')
    budget = request.args.get('budget')
    mood = request.args.get('mood')
    duration = request.args.get('duration')
    vote = request.args.get('vote')
    popularity = request.args.get('popularity')

    data = get_movies(year, budget, mood, duration, vote, popularity)

    response = flask.jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True)
