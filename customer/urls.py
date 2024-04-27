# All necessary imports for creating urls.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Importing all views from this app.
from .views import (personal_document_list,
                    personal_document_details,
                    customer_list,
                    customer_details,)

#-----------------------------------------------------------------------------------------------------------------------

# Creating al necessary url pattern, so that we can access them from internet. .
urlpatterns = [
    path('pd-list', personal_document_list, name='personal-document-list'),
    path('pd-list/<int:pk>', personal_document_details, name='personal-document-details'),

    path('cus-list', customer_list, name='customer-list'),
    path('cus-list/<int:pk>', customer_details, name='customer-details'),
]

#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = format_suffix_patterns(urlpatterns)
#`format_suffix_patterns` helps your API understand different formats like JSON or XML. It allows clients to ask for
# data in their preferred format like `.json` or `.xml`. And in return, clients get data in the way they need it without
# extra negotiation steps.
# In associated views 'format=None' is added for the same purpose.

#-----------------------------------------------------------------------------------------------------------------------
