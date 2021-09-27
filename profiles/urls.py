from django.urls import path
from . import views

# Matching the requested URL to the correct view.

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'),
]
