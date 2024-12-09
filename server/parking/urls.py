from django.urls import path
'''from .views import CarList

urlpatterns = [
    path('parking/', CarList.as_view(), name='car-list'),
]
'''
from .views import FilteredList

urlpatterns = [
    path('filter/', FilteredList.as_view(), name='filtered-list'),
]
