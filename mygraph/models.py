from django.db import models

# Create your models here.
# cookbook/ingredients/models.py

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        'Category', related_name="books", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
