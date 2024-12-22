from django.urls import path

from .views import sendBid

urlpatterns = [
    path('bid/', sendBid.as_view(), name='bid'),
]
