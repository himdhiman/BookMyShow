from django.contrib import admin
from movies import models

# Register your models here.

admin.site.register([
    models.Movie,
    models.Language,
    models.Star,
    models.Genre
])
