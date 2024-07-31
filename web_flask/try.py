#!/usr/bin/python3
"""App 2"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def Display_states():
    """Display States by name"""
    States = storage.all("State")
    sorted_States = sorted(States.values(), key=lambda state: state.name)
    from models.amenity import Amenity
    # Assuming `session` is your SQLAlchemy session
    amenities = storage.all(Amenity)
    
    print(amenities)
    return amenities


@app.teardown_appcontext
def tear(exc):
    """Closes the current sqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
