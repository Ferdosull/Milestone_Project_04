from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime, now


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(('email'), null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
