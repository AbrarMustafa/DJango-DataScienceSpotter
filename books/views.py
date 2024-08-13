from django.db.models import Q
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Book, Profile
from .serializers import BookSerializer
from .services import recommend_books 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter] 
    search_fields = ['title', 'author__name'] 

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated] 
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly] 
        return super().get_permissions()
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Search by title or author", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', None)
        if search:
            self.queryset = self.queryset.filter(
                Q(title__icontains=search) | Q(author__name__icontains=search)
            )
        return super().list(request, *args, **kwargs)
    

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

        if user.profile.favorite_books.count() >= 20:
            return Response({'error': 'You can only have up to 20 favorite books.'}, status=status.HTTP_400_BAD_REQUEST)

        user.profile.favorite_books.add(book)
        return Response({'status': 'Book added to favorites'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user
        book = get_object_or_404(Book, pk=pk)
        user.profile.favorite_books.remove(book)
        return Response({'status': 'Book removed from favorites'}, status=status.HTTP_200_OK)

class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user_profile = user.profile  # Ensure the profile exists
        except Profile.DoesNotExist:
            return Response({"error": "User profile does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        recommendations = recommend_books(user)

        serializer = BookSerializer(recommendations, many=True)
        book_data = serializer.data
        return Response(book_data, status=status.HTTP_200_OK)
