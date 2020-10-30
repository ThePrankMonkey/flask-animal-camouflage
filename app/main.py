from flask import Flask
from flask import render_template, session, redirect, request
import random
import time

from animals import camo, expose

app = Flask(__name__)

CAMO_COUNT = 10
EXPOSE_COUNT = 2


@app.route("/")
def index():
    random.seed(time.time())
    random.shuffle(camo)
    random.shuffle(expose)
    shuffled_animals = camo[:CAMO_COUNT] + expose[:EXPOSE_COUNT]
    random.shuffle(shuffled_animals)

    template_vars = {
        "selected_animals": shuffled_animals,
    }
    print(shuffled_animals[0].__dict__)
    print(shuffled_animals)
    return render_template("index.html", **template_vars)
