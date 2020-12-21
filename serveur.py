#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def requeste():
    response = requests.get('http://127.0.0.1:8000/api/v1/titles?imdb_score_min=9.6&year=2017')
    best_film = response.json()
    url_best_film_details = best_film['results'][0]['url']
    response = requests.get(url_best_film_details)
    best_film_details = response.json()

    list_dic_best_movies = []
    list_best_movies_json = []
    payload = {"imdb_score_min": "9.35",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    best_movies = response.json()
    for i in range((len(best_movies['results']))):
        response = requests.get((best_movies['results'][i]['url']))

        list_dic_best_movies.append(response.json())
    best_movies = list_dic_best_movies[:-3]

    list_dic_familly = []
    payload = {"genre": "Family",
               "imdb_score_min": "8.9",
               "page_size": "7"}

    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    genre_film = response.json()

    for i in range((len(genre_film['results']))):
        response = requests.get((genre_film['results'][i]['url']))
        list_dic_familly.append(response.json())
    categorie_familly = list_dic_familly[:-3]

    return render_template("index.html", best_film=best_film_details,
                           categories_familly=categorie_familly,
                           all_best_movies=best_movies)


@app.route("/best_movies/")
def api_best_movies():
    list_dic_best_movies = []
    payload = {"imdb_score_min": "9.35",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    best_movies = response.json()
    for i in range((len(best_movies['results']))):
        response = requests.get((best_movies['results'][i]['url']))
        list_dic_best_movies.append(response.json())
    return jsonify(list_dic_best_movies)


@app.route("/familly/")
def api_familly():
    list_dic_familly = []
    payload = {"genre": "Family",
               "imdb_score_min": "8.9",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    genre_film = response.json()
    for i in range((len(genre_film['results']))):
        response = requests.get((genre_film['results'][i]['url']))
        list_dic_familly.append(response.json())
    return jsonify(list_dic_familly)


if __name__ == "__main__":
    app.run(debug=True)
