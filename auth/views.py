from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.



# This view is Created for handling errors in the form .......

class Dirtyexception(Exception):
    def __init__(self, error_list):
        self.error_list = error_list


# This view redirects the user where he can choose weather to Login or Signup the app ......

class LoginSignup(TemplateView):
    template_name = 'auth/login-signup.html'


# This is Login Functional View which authenticate the user to the app

def Login(request):
    error = ""
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Incorrect Username or Password"
        context = {
            'error': error
        }
        return render(request, 'auth/login.html', context)
    else:
        return render(request, 'auth/login.html')


# This is the Logout Functional View which Redirects the user to the HomePage after Logging Out .....

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# This is the SignUp Functional View which helps the user to create an account on this webApp ....

def SignUp(request):
    error = ""
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        e1 = e2 = e3 = ''
        try:
            if username == '':
                e1 = 'Username is necessory'
            if email == '':
                e2 ='Email is necessory'
            if password == '':
                e3 ='Password is necessory'
            if e1 != '' or e2 != '' or e3 != '':
                error = [e1, e2, e3]
                raise Dirtyexception(error)
            User.objects.get(username = username)
        except Dirtyexception as err:
            context = {
                "error1": err.error_list[0],
                "error2": err.error_list[1],
                "error3": err.error_list[2]
            }
            return render(request, 'auth/signup.html', context)
        except :
            user = User.objects.create_user(username, email, password)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return render(request, 'auth/afterSignup.html')
        error = "Username already exists"
        context = {
            "error": error
        }
        return render(request, 'auth/signup.html', context)  
    else:
        return render(request, 'auth/signup.html')
