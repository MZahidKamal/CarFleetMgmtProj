# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import AddressModel, PersonModel, EmployeeModel, CompanyModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        # fields = '__all__'
        fields = ['id', 'street', 'house', 'zip_code', 'city', 'state', 'country']

#-----------------------------------------------------------------------------------------------------------------------
