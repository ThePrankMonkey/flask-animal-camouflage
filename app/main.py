from flask import Flask
from flask import render_template, session, redirect, request
import time
import json
import os
import random
import time

from animals import camo, expose

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET") or "some-dummy-string-for-testing"
CAMO_COUNT = 10
EXPOSE_COUNT = 2


@app.route("/")
def index():
    if session.get("animals", False):
        # Game in session
        print("Getting time for last animal")
        last_time = session["timestamp"]
        new_time = time.time()
        diff_time = new_time - last_time
        if session["last_type"] == "camo":
            session["camo_times"].append(diff_time)
        else:
            session["expose_times"].append(diff_time)
        session["timestamp"] = new_time
        print(f"Camo Times:   {session['camo_times']}")
        print(f"Expose Times: {session['expose_times']}")
        print(f"There are {len(session['animals'])} animals in the session")
        animal = json.loads(session.get("animals").pop())
        session["last_type"] = animal["animal_type"]
        session.modified = True
        print(f"Working on {animal['name']} with path {animal['filepath']}")
        return render_template("index.html", animal=animal)
    elif session.get("camo_times"):
        print("Game is over")
        # get average times
        camo_times = session.get("camo_times")
        camo_average = sum(camo_times) / len(camo_times)
        camo_average = round(camo_average, 2)
        expose_times = session.get("expose_times")
        expose_average = sum(expose_times) / len(expose_times)
        expose_average = round(expose_average, 2)
        # reset average times
        session["camo_times"] = []
        session["expose_times"] = []
        return render_template(
            "index.html", camo_average=camo_average, expose_average=expose_average
        )
    else:
        print("There are no animals in the session")
        # check if new game or just finished
        random.seed(time.time())
        random.shuffle(camo)
        random.shuffle(expose)
        shuffled_animals = camo[:CAMO_COUNT] + expose[:EXPOSE_COUNT]
        random.shuffle(shuffled_animals)
        animal = shuffled_animals.pop()
        template_vars = {
            "animal": animal,
        }
        session["animals"] = [a.json() for a in shuffled_animals]
        session["camo_times"] = []
        session["expose_times"] = []
        session["last_type"] = animal.animal_type
        session["timestamp"] = time.time()
        session.modified = True
        print(f"Session has {len(session['animals'])} more animals")
        return render_template("index.html", **template_vars)


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")