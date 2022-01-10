from flask import Flask, render_template, Response, request, redirect, url_for
import logging.config

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'])
def index():
    return "index"


if __name__ == "__main__":
    logging.config.fileConfig('logging.ini',
                              disable_existing_loggers=False)
    logger = logging.getLogger("Main")
    app.run(debug=True)
