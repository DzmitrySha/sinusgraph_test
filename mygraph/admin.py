# Register your models here.
from django.contrib import admin
from mygraph.models import Category, Book

admin.site.register(Category)
admin.site.register(Book)
