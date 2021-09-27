from django.urls import path
from .views import BlogView
from . import views

# Matching the requested URL to the correct view.

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:post_id>', views.detail, name='article-detail'),
    path('add_blog/', views.add_blog_post, name='add_blog'),
    path('edit_blog/<int:post_id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:post_id>', views.delete_blog, name='delete_blog'),
    path(
        'comment/delete_comment/<int:comment_id>/',
        views.delete_comment, name='delete_comment'),
]
