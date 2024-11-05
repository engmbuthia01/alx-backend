#!/usr/bin/env python3
"""
Setting up configuration
settings
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


# Config class with languages and Babel settings
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

# Instantiate Babel
babel = Babel(app)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
