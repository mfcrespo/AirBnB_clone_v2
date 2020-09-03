#!/usr/bin/python3
"""
This module starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
The route /: display "Hello HBNB!"
The route /hbnb: display "HBNB"
The route /c/<text>: display C  followed by the value of the text variable
(replace underscore _ symbols with a space )
The route /python/(<text>): display Python , followed by the value of the
text variable (replace underscore _ symbols with a space )
The route /number/<n>: display n is a number only if n is an integer
The route /number_template/<n>: display a HTML page only if n is an integer
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """
    Prints a message when the route / is taken in the web application
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def greeting2():
    """
    Prints a message when the route / is taken in the web application
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Ctext(text):
    """
    display C  followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pytext(text="is cool"):
    """ Prints Python followed by text that was entered """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def Numberonly(n):
    """ Prints the number followed by 'is a number' """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays an HTML page only if n is a number """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
