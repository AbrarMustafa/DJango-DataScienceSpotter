from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RecommendationView

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('books/recommend/', RecommendationView.as_view(), name='book-recommendations'),
]

# Include router URLs
urlpatterns += router.urls
