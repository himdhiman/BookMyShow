from django.contrib import admin

# Register your models here.

from cinema import models

admin.site.register([
    models.Theatre,
    models.Show
])