#!/usr/bin/python3
"""My first module Using Flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """Displaying My first Page"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
