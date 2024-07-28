#!/usr/bin/python3
"""App 2"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def Display_states():
    """Display States by name"""
    States = storage.all("State")
    return render_template("7-states_list.html", States=States)


@app.route("/cities_by_states", strict_slashes=False)
def Display_states():
    """Display States by name"""
    States = storage.all("State")
    sorted_States = sorted(States.values(), key=lambda state: state.name)

    return render_template("8-cities_by_states.html", States=sorted_States)


@app.teardown_appcontext
def tear(exc):
    """Closes the current sqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
