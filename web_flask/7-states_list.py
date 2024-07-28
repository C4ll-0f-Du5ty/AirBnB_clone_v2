#!/usr/bin/python3
"""App 2"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

myData = storage.all()


@app.route("/states_list", strict_slashes=False)
def Display_states():
    States = storage.all("State")
    return render_template("7-states_list.html", States=States)


@app.teardown_appcontext
def tear():
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
