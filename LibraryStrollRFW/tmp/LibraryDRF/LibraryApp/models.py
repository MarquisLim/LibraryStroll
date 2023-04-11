from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=255)
    describe = models.TextField(blank=True)
    photo = models.ImageField(upload_to='IMG', blank=True)

    def __str__(self):
        return self.name
    
class Genres(models.Model):
    title = models.CharField(max_length=255)
    describe = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='IMG_book', blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    genres = models.ManyToManyField('Genres')
    rating = models.IntegerField(default=0, blank=True, null=True, choices=((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),))
    date_create = models.DateField(default=datetime.now)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
class UserBook(models.Model):
    BOOK_STATUS_CHOICES = (
        ('planned', 'Запланированная книга'),
        ('read', 'Прочитанная книга'),
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=BOOK_STATUS_CHOICES)

# Create your models here.
