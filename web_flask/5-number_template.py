#!/usr/bin/python3
"""
A simple Flask application demonstrating various routing capabilities.
"""

from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)

# Configuring Flask app to accept both /route and /route/
app.config['strict_slashes'] = False

@app.route('/', defaults={'text': ''})
@app.route('/<text>')
def home(text):
    """
    Home route handler.
    
    Displays "Hello HBNB!" when the root URL ("/") is accessed.
    If a text parameter is provided, it displays "Hello HBNB!" followed by the text.
    
    Args:
        text (str, optional): Additional text to append to the greeting. Defaults to ''.
        
    Returns:
        str: Greeting message.
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """
    Route handler for '/hbnb'.
    
    Displays "HBNB" when the '/hbnb' URL is accessed.
    """
    return "HBNB"

@app.route('/c/<text>')
def c_route(text):
    """
    Route handler for '/c/<text>'.
    
    Displays "C " followed by the value of the text variable,
    replacing underscores (_) with spaces.
    
    Args:
        text (str): The text to display, with underscores replaced by spaces.
        
    Returns:
        str: Formatted string.
    """
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>')
def python_route(text):
    """
    Route handler for '/python/<text>'.
    
    Displays "Python " followed by the value of the text variable,
    replacing underscores (_) with spaces.
    
    Args:
        text (str): The text to display, with underscores replaced by spaces.
        
    Returns:
        str: Formatted string.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>')
def number(n):
    """
    Route handler for '/number/<n>'.
    
    Displays "{n} is a number" if n is an integer.
    
    Args:
        n (int): The number to check.
        
    Returns:
        str: Confirmation that n is a number.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Route handler for '/number_template/<n>'.
    
    Renders an HTML page displaying "Number: n" if n is an integer.
    
    Args:
        n (int): The number to display.
        
    Returns:
        str: Rendered HTML page.
    """
    escaped_n = escape(str(n))
    return render_template('number.html', n=escaped_n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)