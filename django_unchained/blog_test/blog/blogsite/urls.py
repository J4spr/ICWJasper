from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="index"),
    # <int:pk> is een primary key, we geven die automatisch mee aan view als context
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="article"),
    path("form", views.ArticleFormView.as_view(), name="articleform"),
    path("form", views.ArticleFormView.as_view(), name="articleform"),
]

urlpatterns += [
    path("login", views.MyLoginView.as_view(), name="login"),
    path("signup", views.MySignupView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
]
