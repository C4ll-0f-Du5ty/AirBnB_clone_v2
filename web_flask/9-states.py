#!/usr/bin/python3
"""App 2"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def Display_states():
    """Display States by name"""
    States = storage.all("State")
    return render_template("9-states.html", States=States)


@app.route("/states/<id>", strict_slashes=False)
def Display_statesByCities(id):
    """Display States by name"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)

    return render_template("9-states.html")


@app.teardown_appcontext
def tear(exc):
    """Closes the current sqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
