from django.urls import path
from .views import BlogView, ArticleDetailView
from . import views

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_blog/', views.add_blog_post, name='add_blog'),
]
