from django.conf.urls import url
from django.urls import path
from cinema.views import TheatreListView, theatre_details

app_name = 'cinema'

urlpatterns = [
    url('', TheatreListView.as_view(), name = 'theatre_list'),
    url('<int:theatre_id>/', theatre_details, name = 'theatre') 
]