# All necessary imports for creating urls.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Importing all views from this app.
from .views import (delivery_agent_list,
                    delivery_agent_details,)

#-----------------------------------------------------------------------------------------------------------------------

# Creating al necessary url pattern, so that we can access them from internet. .
urlpatterns = [
    path('da-list', delivery_agent_list, name='delivery-agent-list'),
    path('da-list/<int:pk>', delivery_agent_details, name='delivery-agent-details'),
]

#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = format_suffix_patterns(urlpatterns)
#`format_suffix_patterns` helps your API understand different formats like JSON or XML. It allows clients to ask for
# data in their preferred format like `.json` or `.xml`. And in return, clients get data in the way they need it without
# extra negotiation steps.
# In associated views 'format=None' is added for the same purpose.

#-----------------------------------------------------------------------------------------------------------------------
