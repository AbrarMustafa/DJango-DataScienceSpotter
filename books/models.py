from django.db import models
from authors.models import Author
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    page_count = models.IntegerField()
    cover_url = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=50)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField(Book, related_name='favored_by')