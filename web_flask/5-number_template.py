from flask import Flask, escape, render_template

app = Flask(__name__, strict_slashes=False)

@app.route('/', defaults={'text': ''})
@app.route('/<text>')
def home(text):
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c_route(text):
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>')
def python_route(text):
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>')
def number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)