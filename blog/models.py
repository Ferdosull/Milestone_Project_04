from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime, now


# Admin blog post model
class Post(models.Model):
    """
    This model is for blog posts which include the user,
    the title, an image or url image, the body text, date & time it was created,
    an alternate submission name and an email name for contact.
    The ordering display is by date.
    """

    class Meta:
        ordering = ['-date']

    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    alternate_submit_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(('email'), null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


# Admin/User Comments model
class Comment(models.Model):
    """
    This is a model for creating blog comments on the actual blog posts.
    The model includes the user making the comment, the post they are commenting on,
    the comment itself and the date/time the comment was made.
    The ordering is "Oldest post first/newest post last",
    similar to a messaging app conversation. This is to allow
    for response comments by the admin if required.
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                  related_name='comments')
    comments = models.TextField(max_length=1000, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Comment made on {self.post.title} by {self.author}"