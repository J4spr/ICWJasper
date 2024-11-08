from random import choices
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django import forms

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, help_text="Enter a title for a new article")
    text = models.CharField(max_length=2500, help_text="Enter text for a new article")
    author = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("model_detail", args={"pk": self.pk})


GENDER_CHOICES = [('man', 'm'), ('vrouw', 'v'), ('ergens ertussen', 'x')]

class User(models.Model):
    name = models.CharField(max_length=250, help_text="Enter first name")
    surname = models.CharField(max_length=250, help_text="Enter last name")
    about = models.CharField(max_length=2000, help_text="Tell us about yourself")
    email = models.EmailField(null=True, blank=True)
    pronoun = forms.ChoiceField(choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"
