import os
import random
from datetime import datetime
from faker import Faker
from django.core.management.base import BaseCommand
from books.models import Book
from authors.models import Author  # Import Author model

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with initial book data'

    def handle(self, *args, **kwargs):
        # Number of books to seed
        num_books = 10000
        
        for i in range(num_books):
            # Generate random values
            author_id = (i + 1) * 10  # Increment author_id by 10
            title = fake.sentence(nb_words=3)[:255]  # Ensure title length is within limit
            genre = fake.word()[:50]  # Ensure genre length is within limit
            isbn = fake.isbn13()[:13]  # Ensure ISBN is 13 characters long
            published_date = fake.date_this_decade()
            page_count = random.randint(100, 500)
            cover_url = fake.image_url()[:255]  # Ensure URL length is within limit
            language = fake.language_code()[:10]  # Ensure language length is within limit
            summary = fake.text(max_nb_chars=500)[:500]  # Ensure summary length is within limit
            
            # Check if the author exists
            if not Author.objects.filter(id=author_id).exists():
                self.stdout.write(self.style.WARNING(f'Skipping book with author_id {author_id}: Author does not exist'))
                continue  # Skip to the next book

            # Create or update the book record
            try:
                book, created = Book.objects.update_or_create(
                    title=title,
                    defaults={
                        "author_id": author_id,
                        "genre": genre,
                        "isbn": isbn,
                        "published_date": published_date,
                        "page_count": page_count,
                        "cover_url": cover_url,
                        "language": language,
                        "summary": summary,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added book "{title}"'))
                else:
                    self.stdout.write(self.style.WARNING(f'Book "{title}" already exists'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating/updating book "{title}": {e}'))
        
        self.stdout.write(self.style.SUCCESS('Book seeding completed.'))
