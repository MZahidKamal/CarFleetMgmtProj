# All necessary imports for creating urls.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Importing all views from this app.
from .views import address_list, address_detail

#-----------------------------------------------------------------------------------------------------------------------

# Creating al necessary url pattern, so that we can access them from internet. .
urlpatterns = [
    path('addresses', address_list, name='addresses'),
    path('addresses/<int:pk>', address_detail, name='address'),
]

#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = format_suffix_patterns(urlpatterns)
#`format_suffix_patterns` helps your API understand different formats like JSON or XML. It allows clients to ask for
# data in their preferred format like `.json` or `.xml`. And in return, clients get data in the way they need it without
# extra negotiation steps.
# In associated views 'format=None' is added for the same purpose.

#-----------------------------------------------------------------------------------------------------------------------
