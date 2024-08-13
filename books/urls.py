from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RecommendationView, FavoriteBookView

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('favorites/<int:pk>/', FavoriteBookView.as_view(), name='favorite-book'),
    path('recommendations/', RecommendationView.as_view(), name='book-recommendations'),
]

# Include router URLs
urlpatterns += router.urls
