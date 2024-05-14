# All necessary imports for creating urls.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Importing all views from this app.
from .views import (common_account_registration_view,
                    common_account_login_view,
                    common_account_logout_view,)

#-----------------------------------------------------------------------------------------------------------------------

# Creating al necessary url pattern, so that we can access them from internet. .
urlpatterns = [
    path('ac-registration', common_account_registration_view, name='common-account-registration'),
    path('ac-login', common_account_login_view, name='common-account-login'),
    path('ac-logout', common_account_logout_view, name='common-account-logout'),
]

#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = format_suffix_patterns(urlpatterns)
#`format_suffix_patterns` helps your API understand different formats like JSON or XML. It allows clients to ask for
# data in their preferred format like `.json` or `.xml`. And in return, clients get data in the way they need it without
# extra negotiation steps.
# In associated views 'format=None' is added for the same purpose.

#-----------------------------------------------------------------------------------------------------------------------
