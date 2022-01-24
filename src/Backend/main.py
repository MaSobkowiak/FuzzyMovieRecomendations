from src.helper import create_app, get_movies, get_semantic
import flask
from flask import request

app = create_app()


@app.route("/movies", methods=['GET'])
def movies():
    year = get_semantic(request.args.get('year'))
    budget = get_semantic(request.args.get('budget'))
    mood = get_semantic(request.args.get('mood'))
    duration = get_semantic(request.args.get('duration'))
    vote = get_semantic(request.args.get('vote'))
    popularity = get_semantic(request.args.get('popularity'))

    data = get_movies(year, budget, mood, duration, vote, popularity)

    response = flask.jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True)
