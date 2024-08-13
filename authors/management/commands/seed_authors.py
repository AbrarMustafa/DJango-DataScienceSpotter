import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from books.models import Author

class Command(BaseCommand):
    help = 'Seed the database with initial author data from a JSON-like file where each line is a JSON object'

    def handle(self, *args, **kwargs):
        # Path to the file
        file_path = os.path.join(settings.BASE_DIR, 'data', 'authors.json')

        # Open and read the file line by line
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Skip any empty lines
                    try:
                        # Parse each line as a JSON object
                        author_data = json.loads(line.strip())

                        # Create or get the Author object
                        author, created = Author.objects.get_or_create(
                            id=author_data["id"],
                            defaults={
                                "name": author_data["name"],
                                "gender": author_data["gender"],
                                "image_url": author_data["image_url"],
                                "about": author_data["about"],
                                "ratings_count": author_data["ratings_count"],
                                "average_rating": author_data["average_rating"],
                                "text_reviews_count": author_data["text_reviews_count"],
                                "works_count": author_data["works_count"],
                                "fans_count": author_data["fans_count"],
                            }
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Successfully added author {author.name}'))
                        else:
                            self.stdout.write(self.style.WARNING(f'Author {author.name} already exists'))

                    except json.JSONDecodeError as e:
                        self.stdout.write(self.style.ERROR(f'Failed to parse line: {line}. Error: {e}'))

        self.stdout.write(self.style.SUCCESS('Author seeding completed.'))
