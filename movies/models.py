from django.db import models
from django.urls.base import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

# Create your models here.

class MovieQuerySet(models.query.QuerySet):
    def search(self,query):
        lookup = (
            Q(Title__icontains=query)
        )
        return self.filter(lookup).distinct()

class MovieManager(models.Manager):
    def get_queryset(self):
        return MovieQuerySet(self.model,self._db)
    def search(self,query):
        return self.get_queryset().search(query)


class Movie(models.Model):

    rating_choice = (
            ('U', 'U'),
            ('UA', 'U/A'),
            ('A', 'A'),
            ('R', 'R'),
        )
    Title = models.CharField(max_length = 256)
    Description = models.TextField()
    Rating = models.FloatField(validators = [MaxValueValidator(10), MinValueValidator(0)], null = True)
    Run_Length = models.IntegerField(help_text="Enter run length in minutes")
    Genres = models.ManyToManyField('Genre')
    Languages = models.ManyToManyField('Language')
    popularity_index  = models.IntegerField(unique=True,null=True,blank=True)
    certificate = models.CharField(max_length=2,choices=rating_choice)
    Poster_Link = models.URLField(max_length = 256, null = 'True')
    Hor_Poster_Link = models.URLField(max_length = 256, null = 'True')
    Trailer_link = models.CharField(max_length = 256, null = 'True')
    ReleaseDate = models.DateField(null = True)
    stars = models.ManyToManyField('Star')

    objects = MovieManager()

    def get_absolute_url(self):
        return reverse('movie', kwargs = {'movie_id' : self.pk})

    def __str__(self):
        return self.Title    

class Language(models.Model):
    lang = models.CharField(max_length = 20)

    def __str__(self):
        return self.lang

class Star(models.Model):
    star = models.CharField(max_length = 50)

    def __str__(self):
        return self.star

class Genre(models.Model):
    genre = models.CharField(max_length = 20)

    def __str__(self):
        return self.genre
