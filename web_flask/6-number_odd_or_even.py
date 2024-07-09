#!/usr/bin/python3
"""Had to use werzeug utils cause it wasnt in the flask import cause the flask version"""
from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb_hbnb():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    text = escape(text).replace('_', ' ')
    return ("C {}".format(text))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def hbnb_python(text):
    text = escape(text).replace('_', ' ')
    return ("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def hbnb_number(n):
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return (render_template("5-number.html", num=n))
    else:
        return ("Not found", 404)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            odev = "even"
        else:
            odev = "odd"
        return (render_template("6-number_odd_or_even.html", num=n, odev=odev))
    else:
        return ("Not found", 404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)