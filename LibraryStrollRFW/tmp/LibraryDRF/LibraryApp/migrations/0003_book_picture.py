# Generated by Django 4.2 on 2023-04-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0002_genres_book_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, upload_to='IMG_book'),
        ),
    ]
