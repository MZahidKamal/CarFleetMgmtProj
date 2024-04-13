# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import CarModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------
