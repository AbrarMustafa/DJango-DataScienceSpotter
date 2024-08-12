from .models import Book

def recommend_books(user):
    """
    Generate a list of recommended books based on the user's favorite books.
    
    Args:
    - user: The user for whom the recommendations are being generated.

    Returns:
    - A queryset of Book objects that are recommended for the user.
    """
    # Get the user's favorite books
    favorite_books = user.profile.favorite_books.all()

    # Example logic: Recommend books that are in the same genre as the favorite books
    recommended_books = Book.objects.filter(genre__in=[book.genre for book in favorite_books]).exclude(id__in=favorite_books.values_list('id', flat=True))

    # Limit the number of recommendations
    return recommended_books.distinct()[:5]
