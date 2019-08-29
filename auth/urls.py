from django.urls import path

from auth import views

urlpatterns = [
    path('', views.LoginSignup.as_view(), name = 'loginsignup'),
    path('login/', views.Login, name = 'login'),
    path('signup/', views.SignUp, name = 'signup'),
    path('logout/', views.Logout, name = 'logout')
]