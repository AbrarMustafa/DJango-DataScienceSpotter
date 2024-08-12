from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, AuthorViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

# Include router URLs
urlpatterns += router.urls
