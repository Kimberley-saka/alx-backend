#!/usr/bin/env python3
"""
flask app
"""
from flask_babel import Babel
from flask import Flask, render_template


class config(object):
    """
    config languages etc
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """
    basic flask app
    """

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
