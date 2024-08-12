from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import BookViewSet, FavoriteBookView

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router
urlpatterns = router.urls

# Add additional URL patterns that aren't handled by the router
urlpatterns += [
    path('books/<int:pk>/favorite/', FavoriteBookView.as_view(), name='favorite-book'),
    path('recommendations/', BookViewSet.as_view({'get': 'recommendations'}), name='recommendations'),
]
