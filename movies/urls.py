from django.urls import path
from movies import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('<int:movie_id>/', views.Movie, name = 'movie')
]