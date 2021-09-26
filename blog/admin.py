from django.contrib import admin
from .models import Post, Comment

# Registering the Post and Comment models.

admin.site.register(Post)
admin.site.register(Comment)
