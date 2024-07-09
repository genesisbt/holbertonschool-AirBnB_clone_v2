#!/usr/bin/python3
"""Script"""
from flask import Flask, render_template


wapp = Flask(__name__)


@wapp.route('/', strict_slashes=False)
def greetings():
    return "Hello HBNB!"


@wapp.route('/hbnb', strict_slashes=False)
def greet_hbnb():
    return "HBNB"


@wapp.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@wapp.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@wapp.route('/python/<text>', strict_slashes=False)
def py_route(text):
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


@wapp.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    return ("{} is a number".format(n))


@wapp.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    return (render_template('5-number.html', n=n))


if __name__ == "__main__":
    wapp.run(host='0.0.0.0', port=5000)