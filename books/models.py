from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    page_count = models.IntegerField()
    cover_url = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
