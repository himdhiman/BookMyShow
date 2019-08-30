from django.conf.urls import url
from django.urls import path
from tickets import views

# app_name = 'tickets'

urlpatterns = [
    path('seatchoice/<int:show_id>/', views.reserve_seat, name = "Reserve"),
    path('payment/', views.payment_gateway, name='payment_gateway'),
    path('payment_confirmation/', views.payment_confirmation, name = 'payment_confirmation'),
    path('', views.BookingListView.as_view(), name = 'list'),
    path('<int:btid>/delete/', views.BookingDeleteView.as_view(), name = 'delete'),
    path('<int:btid>/', views.BookingDetailView.as_view(), name = 'detail')
]