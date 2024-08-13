from django.db import models
from authors.models import Author
from django.contrib.auth.models import User

class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)  # Example length
    isbn = models.CharField(max_length=13)  # Example length
    published_date = models.DateField()
    page_count = models.PositiveIntegerField()
    cover_url = models.URLField(max_length=255, blank=True, null=True)  # Example length
    language = models.CharField(max_length=10, blank=True, null=True)  # Example length
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField(Book, related_name='favored_by')

    def __str__(self):
        return self.user.username