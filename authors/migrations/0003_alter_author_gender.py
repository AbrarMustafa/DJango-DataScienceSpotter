# Generated by Django 4.2.15 on 2024-08-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_about_author_average_rating_author_fans_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(default='unknown', max_length=30),
        ),
    ]
