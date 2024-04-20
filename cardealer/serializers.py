# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import CarDealerModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
class CarDealerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealerModel
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------
