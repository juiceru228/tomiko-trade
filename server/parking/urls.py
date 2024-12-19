from django.urls import path

from .views import FilteredList

urlpatterns = [
    path('filter/', FilteredList.as_view(), name='filtered-list'),
]
