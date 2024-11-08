from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("forces/", views.homepageview, name="homepage"),
    path("forces/training", views.trainingview, name="training"),
    path("forces/about", views.aboutview, name="about"),
    path("forces/contact", views.contactview, name="contact"),
    path("forces/articles", views.articleview, name="articles"),
]


urlpatterns += [
    path("forces/login", views.MyLoginView.as_view(), name="login"),
    path("signup", views.MySignUpView.as_view(), name="signup"),
    path("forces/logout", LogoutView.as_view(), name="logout")
]