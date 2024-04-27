# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import PersonalDocumentsModel, CustomerModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class PersonalDocumentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDocumentsModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------
