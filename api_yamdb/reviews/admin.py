from django.contrib import admin
from .models import (Title, Category,
                     Review, Genre, Comment, User)

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(User)
