from rest_framework import serializers
from .models import Book
from authors.models import Author
from authors.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)

    class Meta:
        model = Book
        fields = '__all__'
