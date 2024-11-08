from django.contrib import admin

from blogsite.models import Article, Contributor

# Register your models here.
admin.site.register(Article)
admin.site.register(Contributor)