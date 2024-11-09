#!/usr/bin/env python3
"""
Setting up configuration
settings
"""
from flask import Flask, render_template, request
from flask_babel import Babel,gettext as _


app = Flask(__name__)


# Config class with languages and Babel settings
class Config:
    """
    application configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Gets locale from request object
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    renders a basic html template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
