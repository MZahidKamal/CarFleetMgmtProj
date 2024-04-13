# All necessary imports for creating urls.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# Importing all views from this app.
from .views import (car_expenses_list,
                    car_expense_details,
                    overhead_expenses_list,
                    overhead_expense_details,
                    work_order_list,
                    work_order_details,
                    )

#-----------------------------------------------------------------------------------------------------------------------

# Creating al necessary url pattern, so that we can access them from internet. .
urlpatterns = [
    path('ce-list', car_expenses_list, name='car-expense-list'),
    path('ce-list/<int:pk>', car_expense_details, name='car-expense-details'),

    path('oe-list', overhead_expenses_list, name='overhead-expense-list'),
    path('oe-list/<int:pk>', overhead_expense_details, name='overhead-expense-details'),

    path('wo-list', work_order_list, name='workorder-list'),
    path('wo-list/<int:pk>', work_order_details, name='workorder-details'),
]

#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = format_suffix_patterns(urlpatterns)
#`format_suffix_patterns` helps your API understand different formats like JSON or XML. It allows clients to ask for
# data in their preferred format like `.json` or `.xml`. And in return, clients get data in the way they need it without
# extra negotiation steps.
# In associated views 'format=None' is added for the same purpose.

#-----------------------------------------------------------------------------------------------------------------------
