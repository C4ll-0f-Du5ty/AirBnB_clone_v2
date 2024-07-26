#!/usr/bin/python3
"""App 2"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """Displaying My first Page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HelloHBNB():
    """Displaying my second Page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def Display_C(text):
    """Displaying my third Page"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def Display_Python(text="is cool"):
    """Displaying my Fourth Page"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:text>", strict_slashes=False)
def Display_Number(text):
    """Displaying my Fourth Page"""
    return f"{text} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
