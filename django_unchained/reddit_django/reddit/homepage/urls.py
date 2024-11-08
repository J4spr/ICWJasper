from django.urls import path

from . import views

urlpatterns = [
    path("reddit/", views.homepageview, name="index"),
	path('reddit/sub', views.subredditview, name="subreddit")
]
