from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Genres)
admin.site.register(Author)
admin.site.register(UserBook)

# Register your models here.
