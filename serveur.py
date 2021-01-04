#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
from requestsAPI import RequestsApi


app = Flask(__name__, static_url_path='/static')

best_film_details = RequestsApi.best_movie()
best_movies = RequestsApi.best_movies()
categorie_familly = RequestsApi.categorie_family()
categorie_horror = RequestsApi.category_horror()
categorie_music = RequestsApi.category_music()


@app.route("/")
def requeste():
    """

    Fonction qui permet de passer au template index.html les differentes catégories de film
    :return: les differentes categories de films
    """
    return render_template("index.html", best_film=best_film_details,
                           categories_familly=categorie_familly,
                           all_best_movies=best_movies,
                           categories_horror=categorie_horror,
                           categories_music=categorie_music)


@app.route("/best_movie/")
def api_best_movie():
    """

    Fonction qui permet de créer un end point pour récuperer le meilleur film en javascipt
    :return:le meilleur film en format jason
    """
    return jsonify(best_film_details)


@app.route("/best_movies/")
def api_best_movies():
    """

    Fonction qui permet de créer un end point pour récuperer les meilleurs films en javascipt
    :return:les  sept meilleurs films d'imdb en format jason
    """
    return jsonify(best_movies)


@app.route("/familly/")
def api_familly():
    """

    Fonction qui permet de créer un end point pour récuperer les meilleurs films de la categorie famille en javascipt
    :return:les  sept meilleurs films d'imdb de la categorie famille en format jason
    """
    return jsonify(categorie_familly)


@app.route("/horror/")
def api_horror():
    """

    Fonction qui permet de créer un end point pour récuperer les meilleurs films de la categorie horror en javascipt
    :return:les  sept meilleurs films d'imdb de la categorie horror en format jason
    """
    return jsonify(categorie_horror)


@app.route("/music/")
def api_music():
    """

    Fonction qui permet de créer un end point pour récuperer les meilleurs films de la categorie music en javascipt
    :return:les  sept meilleurs films d'imdb de la categorie music en format jason
    """
    return jsonify(categorie_music)


if __name__ == "__main__":
    app.run(debug=True)
