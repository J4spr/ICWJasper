import datetime

from django.shortcuts import render

# Create your views here.
subreddit_title = "test"
first_post = {
	"created_at": datetime.datetime(2019, 5, 20, 15, 15, 20),
	"text": "Does a computer run without a cpu",
	"theme": "discussion",
	"comments": [
		"He definitly lost it",
		"Imagine the amount of brain cells this guy has",
	],
}


def subredditview(request):
	context = {"post": first_post, "subreddit_name": subreddit_title}
	return render(request, "homepage/subreddit.html", context=context)

def homepageview(request):
	return render(request, "homepage/homepage.html")
