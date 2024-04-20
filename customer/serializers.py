# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import CustomerModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------
