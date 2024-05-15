#!/usr/bin/python3
"""Starts Flask Web App"""
from flask import Flask


wapp = Flask(__name__)


@wapp.route('/', strict_slashes=False)
def greetings():
    """Method that displays "Hello HBNB!"."""
    return "Hello HBNB!"


@wapp.route('/hbnb', strict_slashes=False)
def greet_hbnb():
    """Method that displays "HBNB"."""
    return "HBNB"


if __name__ == "__main__":
    wapp.run(host='0.0.0.0', port=5000)
