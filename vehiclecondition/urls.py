"""# All necessary imports for creating urls.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Importing all views from this app.
from .views import (vehicle_condition_list,
                    vehicle_condition_detail,
                    car_receiving_vc_list,
                    car_receiving_vc_detail,
                    car_giving_vc_list,
                    car_giving_vc_detail)

#-----------------------------------------------------------------------------------------------------------------------

# Creating al necessary url pattern, so that we can access them from internet. .
urlpatterns = [
    path('vc-list', vehicle_condition_list, name='vc-list'),
    path('vc-list/<int:pk>', vehicle_condition_detail, name='vc-details'),

    path('vc-list-cr', car_receiving_vc_list, name='cr-vc-list'),
    path('vc-list-cr/<int:pk>', car_receiving_vc_detail, name='cr-vc-details'),

    path('vc-list-cd', car_giving_vc_list, name='cd-vc-list'),
    path('vc-list-cd/<int:pk>', car_giving_vc_detail, name='cd-vc-details'),
]

#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = format_suffix_patterns(urlpatterns)
#`format_suffix_patterns` helps your API understand different formats like JSON or XML. It allows clients to ask for
# data in their preferred format like `.json` or `.xml`. And in return, clients get data in the way they need it without
# extra negotiation steps.
# In associated views 'format=None' is added for the same purpose.

#-----------------------------------------------------------------------------------------------------------------------
"""