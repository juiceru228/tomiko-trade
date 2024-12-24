from django.urls import path

from .views import getClips, getReviews

urlpatterns = [
    path('clips/', getClips, name='clips-list'),
    path('reviews/', getReviews, name='reviews-list'),
]
