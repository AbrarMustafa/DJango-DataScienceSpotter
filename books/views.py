from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from .services import recommend_books  # Custom recommendation logic

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Override the create, update, and delete methods to require authentication
    def create(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def recommendations(self, request):
        user = request.user
        recommended_books = recommend_books(user)
        serializer = self.get_serializer(recommended_books, many=True)
        return Response(serializer.data)

class FavoriteBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        book = get_object_or_404(Book, pk=pk)

        # Add the book to the user's favorites
        user.profile.favorite_books.add(book)
        return Response({'status': 'book added to favorites'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user
        book = get_object_or_404(Book, pk=pk)

        # Remove the book from the user's favorites
        user.profile.favorite_books.remove(book)
        return Response({'status': 'book removed from favorites'}, status=status.HTTP_200_OK)

class RecommendationView(APIView):
    def post(self, request):
        user_favorites = request.data.get('favorites', [])  # Expecting a list of book IDs
        recommendations = recommend_books(user_favorites)
        return Response({'recommendations': recommendations}, status=status.HTTP_200_OK)