#!/usr/bin/python3
"""Starts a Flask Web app"""
from flask import Flask

wapp = Flask(__name__)

@wapp.route('/', strict_slashes=False)
def greetings():
    return "Hello HBNB!"

if __name__ == "__main__":
    wapp.run(host='0.0.0.0', port=5000)