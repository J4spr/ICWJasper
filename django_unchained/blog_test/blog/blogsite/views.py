from django.shortcuts import redirect, render
from django.views import generic
from .models import *
from django.forms import ModelForm
from .forms import *
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import ArticleModelForm


# Create your views here.
class ArticleListView(generic.ListView):

    # Listvuew heeft een attr model
    model = Article

    # de naam van de database objecten in je html set
    template_name = "blogsite/article.html"

    # wordt gebruikt door listview en geeft ALLE articles mee
    context_object_name = "articles"

    queryset = Article.objects.all()

    # waar staat de html? (in je eigen files)
    template_name = "blogsite/index.html"

    # paginate_by = 10


class ArticleDetailView(generic.DetailView):
    # detail view heeft enkel een model nodig en een private key
    model = Article

    template_name = "blogsite/article.html"


class ArticleFormView(LoginRequiredMixin, FormView):
    form_class = ArticleModelForm
    template_name = "blogsite/form.html"
    success_url = "/blogsite"
    login_url = 'login'
    redirect_field_name = 'article-form' 

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return super().form_valid(form)


class MySignupView(CreateView):
    # form_class = UserCreationForm
    succes_url = "login"
    template_name = "blogsite/login.html"


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "blogsite/login.html"
