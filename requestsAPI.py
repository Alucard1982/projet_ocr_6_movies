#!/usr/bin/env python3
# -*- coding: utf-8 -*
import requests


class RequestsApi:

    @staticmethod
    def best_movie():
        try:
            response = requests.get('http://127.0.0.1:8000/api/v1/titles?imdb_score_min=9.6&year=2017')
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        best_film = response.json()
        url_best_film_details = best_film['results'][0]['url']
        try:
            response = requests.get(url_best_film_details)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        best_film_details = response.json()
        return best_film_details

    @staticmethod
    def best_movies():
        list_dic_best_movies = []
        payload = {"imdb_score_min": "9.35",
                   "page_size": "7"}
        try:
            response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        best_movies = response.json()
        for i in range((len(best_movies['results']))):
            try:
                response = requests.get((best_movies['results'][i]['url']))
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            list_dic_best_movies.append(response.json())
        best_movies = list_dic_best_movies
        return best_movies

    @staticmethod
    def categorie_family():
        list_dic_familly = []
        payload = {"genre": "Family",
                   "imdb_score_min": "8.9",
                   "page_size": "7"}
        try:
            response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        genre_film = response.json()
        for i in range((len(genre_film['results']))):
            try:
                response = requests.get((genre_film['results'][i]['url']))
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            list_dic_familly.append(response.json())
        categorie_familly = list_dic_familly
        return categorie_familly

    @staticmethod
    def category_horror():
        list_dic_horror = []
        payload = {"genre": "Horror",
                   "imdb_score_min": "8.5",
                   "page_size": "7"}
        try:
            response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        genre_film = response.json()
        for i in range((len(genre_film['results']))):
            try:
                response = requests.get((genre_film['results'][i]['url']))
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            list_dic_horror.append(response.json())
        categorie_horror = list_dic_horror
        return categorie_horror

    @staticmethod
    def category_music():
        list_dic_music = []
        payload = {"genre": "Music",
                   "imdb_score_min": "8.6",
                   "page_size": "7"}
        try:
            response = requests.get('http://127.0.0.1:8000/api/v1/titles', params=payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        genre_film = response.json()
        for i in range((len(genre_film['results']))):
            try:
                response = requests.get((genre_film['results'][i]['url']))
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
            list_dic_music.append(response.json())
        categorie_music = list_dic_music
        return categorie_music
