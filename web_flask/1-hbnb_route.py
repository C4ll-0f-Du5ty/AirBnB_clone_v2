#!/usr/bin/python3
"""App 1"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """Displaying My first page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def Hello1():
    """Displaying my second page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
