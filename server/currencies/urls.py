from django.urls import path

from .views import getCurrencies

urlpatterns = [
    path('currencies/', getCurrencies, name='currencies-list'),
]
