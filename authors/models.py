from django.db import models

class Author(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=30, default='unknown')
    image_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True)
    ratings_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    text_reviews_count = models.IntegerField(default=0)
    works_count = models.IntegerField(default=0)
    fans_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name