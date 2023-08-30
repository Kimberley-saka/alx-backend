#!/usr/bin/env python3
"""
simple flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel



app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    language config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """
    displays hello world
    """
    return render_template('0-index.html')

@babel.localeselector
def get_locale():
    """
    get best matcyh locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
