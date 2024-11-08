from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, help_text="Enter a title for a new article")
    text = models.CharField(max_length=1500, help_text="Enter text for a new article")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("model_detail", args={"pk": self.id})
    
    
    def __str__(self):
        return self.title


class Contributor(models.Model):
    name = models.CharField(max_length=250, help_text="Enter first name")
    surname = models.CharField(max_length=250, help_text="Enter last name")
    about = models.CharField(max_length=2000, help_text="Tell us something about yourself")
    email = models.EmailField(null=True, blank=True)
    class Meta():
        ordering = ["name", "surname"]

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"