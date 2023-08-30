#!/usr/bin/env python3
"""
simple flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, exceptions, utc
from datetime import datetime
import locale


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('index.html')


def get_user():
    """
    get user
    """
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_reqeust():
    """
    runs before other functions
    """
    user = get_user()
    g.user = user

    time_now = utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    time_format = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(time_format)


@babel.localeselector
def get_locale():
    """
    get best match locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    get timezone
    """
    tmzone = request.args.get('timezone', None)
    if tmzone:
        try:
            return timezone(tmzone).zone
        except exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            tmzone = g.user.get('timezone')
            return timezone(tmzone).zone
        except exceptions.UnknownTimeZoneError:
            pass

    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
