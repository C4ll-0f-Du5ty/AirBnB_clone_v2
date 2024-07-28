#!/usr/bin/python3
from flask import Flask, render_template
import sys
from pathlib import Path
from models import storage

# Dynamically add the parent directory of
# 'flask' and 'models' to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

app = Flask(__name__)

# @app.route("/states_list", strict_slashes=False)

print(storage.all())

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)
