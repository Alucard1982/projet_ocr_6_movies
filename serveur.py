#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    messageBienvenue = "Futur développeur Python"
    objectif = "L'objectif de ce projet est d'intéragir avec une API Rest et le front"
    return render_template("index.html", texte=messageBienvenue, message=objectif)


if __name__ == "__main__":
    app.run(debug=True)
