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

    list_dic_horror = []
    payload = {"genre": "Horror",
               "imdb_score_min": "8.5",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    genre_film = response.json()
    for i in range((len(genre_film['results']))):
        response = requests.get((genre_film['results'][i]['url']))
        list_dic_horror.append(response.json())
    categorie_horror = list_dic_horror[:-3]

    list_dic_music = []
    payload = {"genre": "Music",
               "imdb_score_min": "8.6",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    genre_film = response.json()
    for i in range((len(genre_film['results']))):
        response = requests.get((genre_film['results'][i]['url']))
        list_dic_music.append(response.json())
    categorie_music = list_dic_music[:-3]

    return render_template("index.html", best_film=best_film_details,
                           categories_familly=categorie_familly,
                           all_best_movies=best_movies,
                           categories_horror=categorie_horror,
                           categories_music=categorie_music)


@app.route("/best_movie/")
def api_best_movie():
    response = requests.get('http://127.0.0.1:8000/api/v1/titles?imdb_score_min=9.6&year=2017')
    best_film = response.json()
    url_best_film_details = best_film['results'][0]['url']
    response = requests.get(url_best_film_details)
    best_film_details = response.json()
    return jsonify(best_film_details)


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


@app.route("/horror/")
def api_horror():
    list_dic_horror = []
    payload = {"genre": "Horror",
               "imdb_score_min": "8.5",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    genre_film = response.json()
    for i in range((len(genre_film['results']))):
        response = requests.get((genre_film['results'][i]['url']))
        list_dic_horror.append(response.json())
    return jsonify(list_dic_horror)


@app.route("/music/")
def api_music():
    list_dic_music = []
    payload = {"genre": "Music",
               "imdb_score_min": "8.6",
               "page_size": "7"}
    response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
    genre_film = response.json()
    for i in range((len(genre_film['results']))):
        response = requests.get((genre_film['results'][i]['url']))
        list_dic_music.append(response.json())
    return jsonify(list_dic_music)


if __name__ == "__main__":
    app.run(debug=True)
