#!/usr/bin/python3
"""Script that starts a Flask web application"""
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


@wapp.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_odd_even(n):
    if n % 2 == 0:
        od_ev = 'even'
    else:
        od_ev = 'odd'
    return (render_template('6-number_odd_or_even.html', n=n, od_ev=od_ev))


if __name__ == "__main__":
    wapp.run(host='0.0.0.0', port=5000)
