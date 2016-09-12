from os import path
from flask import render_template

from app import app
from app.lib.random_team import RandomGroups


@app.route("/")
def index():

    random_groups = RandomGroups()

    return render_template("index.html", random_groups=random_groups)
    