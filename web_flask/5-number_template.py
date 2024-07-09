#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    text_with_spaces = ' '.join(text.split('_'))
    return f'C {text_with_spaces}'

@app.route('/python/<text>')
def python(text):
    text_with_spaces = ' '.join(text.split('_'))
    return f'Python {text_with_spaces}'

@app.route('/number/<int:n>')
def number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, strict_slashes=False)