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
def Ctext():
    """
    display C  followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
