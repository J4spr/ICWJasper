from django.shortcuts import redirect, render
from django.views import generic
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import *


# Create your views here.
def homepageview(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 2;")
        articles = cursor.fetchall()
    context = {"articles": articles,
               "user": request.user}
    return render(request, "homepage/homepage.html", context=context)


def aboutview(request):
    return render(request, "homepage/about.html")


def articleview(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM articles ORDER BY id DESC")
        articles = cursor.fetchall()
    context = {'articles': articles}
    return render(request, "homepage/articles.html", context=context)


def contactview(request):
    return render(request, "homepage/contact.html")


def trainingview(request):
    return render(request, "homepage/training.html")


def error_404_view(request, exception):
    return render(request, "homepage/404.html")


class MySignUpView(CreateView):
    form_class = UserCreationForm
    succes_url = 'login'
    template_name = 'homepage/signup.html'



class MyLoginView(LoginView):
    redirect_authenticated_user = True 
    authentication_form = AuthenticationForm
    template_name = 'homepage/login.html' 
    success_url = "login"

