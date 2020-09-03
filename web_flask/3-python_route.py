#!/usr/bin/python3
"""
This module starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
The route /: display "Hello HBNB!"
The route /hbnb: display "HBNB"
The route /c/<text>: display C  followed by the value of the text variable
(replace underscore _ symbols with a space )
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
