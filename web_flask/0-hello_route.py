!/usr/bin/python3
"""
This module starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
The route /: display Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """
    Prints a message when the route / is taken in the web application
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
