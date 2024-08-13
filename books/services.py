from .models import Book
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compute_similarity_matrix(books):
    # Example feature vectors for each book (genre, author, etc.)
    features = np.array([[book.genre, book.author] for book in books])
    similarity_matrix = cosine_similarity(features)
    return similarity_matrix

def get_similar_books(book, books, similarity_matrix):
    index = books.index(book)
    similar_indices = similarity_matrix[index].argsort()[-6:-1]  # Top 5 similar books
    return [books[i] for i in similar_indices]


def recommend_books(user):
    # Get the user's favorite books
    favorites = user.profile.favorite_books.all()

    if not favorites:
        return []  # Return an empty list if no favorites

    # Get all books in the database
    books = list(Book.objects.all())
    
    # Compute the similarity matrix
    similarity_matrix = compute_similarity_matrix(books)
    
    # Prepare a list for recommended books
    recommended_books = []

    # Iterate through user's favorite books to find similar ones
    for favorite in favorites:
        similar_books = get_similar_books(favorite, books, similarity_matrix)
        recommended_books.extend(similar_books)
    
    # Remove duplicates and limit to top 5 recommendations
    recommended_books = list(dict.fromkeys(recommended_books))[:5]

    return recommended_books
