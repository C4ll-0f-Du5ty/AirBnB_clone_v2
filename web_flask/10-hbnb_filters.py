#!/usr/bin/python3
"""App 2"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filter", strict_slashes=False)
def Display_states():
    """Display Full Page"""
    States = storage.all(State)
    Amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           States=States, Amenities=Amenities)


@app.teardown_appcontext
def tear(exc):
    """Closes the current sqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
