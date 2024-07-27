#!/usr/bin/python3
"""App 2"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:text>", strict_slashes=False)
def Display_HTML(text):
    """Displaying my Fourth Page"""
    return render_template("5-number.html", Number=text)


@app.route("/number_odd_or_even/<int:text>", strict_slashes=False)
def Display_State(text):
    """Displaying my Fourth Page"""
    state = ""
    if text % 2 == 0:
        state = "even"
    else:
        state = "odd"
    return render_template("6-number_odd_or_even.html",
                           Number=text, State=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
