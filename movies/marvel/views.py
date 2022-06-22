import json
import os

from os.path import join

from django.shortcuts import render


def get_marvel_movies(request):
    template_name = 'marvels/list.html'
    movie_data_file = 'marvel_movies_v2.json'
    movie_data_file_path = join(os.getcwd(), 'marvel', movie_data_file)
    with open(movie_data_file_path, 'r') as infile:
        movies = json.loads(infile.read())
    return render(request, template_name, {
        'movies': movies,
    })
