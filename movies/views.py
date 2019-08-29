from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, View
from movies import models
from cinema.models import Show
import datetime

# Create your views here.

class Index(ListView):

     def get(self, request, *args, **kwars):
          movies_list = models.Movie.objects.all().order_by('popularity_index')
          popular_movies = models.Movie.objects.all().order_by('popularity_index')[:3]
          context = {
               'movies_list' : movies_list,
               'popular_movies' : popular_movies
          }
          return render(request, 'home/index.html', context)

def Movie(request, movie_id):
     movie_details = models.Movie.objects.get(pk = movie_id)
     Lang = movie_details.Languages.all()
     stars = movie_details.stars.all()
     shows = Show.objects.filter(movie=movie_id, date=datetime.date.today()).order_by('theatre')
     show_list = []
     if shows:
          show_by_theatre = []
          theatre = shows[0].theatre
          for i in range(0, len(shows)):
               if theatre != shows[i].theatre:
                    theatre = shows[i].theatre
                    show_list.append(show_by_theatre)
                    show_by_theatre = []
               show_by_theatre.append(shows[i])
          show_list.append(show_by_theatre)
     context = {
     'movie_details' : movie_details,
     'Lang' : Lang,
     'stars' : stars,
     'show_list' : show_list
     }
     return render(request, 'movies/movie.html', context)


