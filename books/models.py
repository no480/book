
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    price = models.FloatField()
    isbn = models.CharField(max_length=13, unique=True)
