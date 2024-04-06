from django.urls import path
from .views import address_list

urlpatterns = [
    path('addresses', address_list, name='addresses'),
]
