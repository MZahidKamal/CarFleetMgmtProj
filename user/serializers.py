# All necessary imports for creating serializers.
from rest_framework import serializers

# Importing all database models from this app.
from .models import (ManufacturerAccountModel,
                     CarDealerAccountModel,
                     DeliveryAgentAccountModel,
                     CustomerAccountModel,)

from manufacturer.models import ManufacturerModel
from cardealer.models import CarDealerModel
from deliveryagent.models import DeliveryAgentModel
from customer.models import CustomerModel
from stationery.models import AddressModel, PersonModel, CompanyModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a serializer so that it can translate the python object into a JSON format.
"""
class ManufacturerAccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerAccountModel
        fields = '__all__'

class CarDealerAccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealerAccountModel
        fields = '__all__'

class DeliveryAgentAccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgentAccountModel
        fields = '__all__'

class CustomerAccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAccountModel
        fields = '__all__'

As there is no field at all in the aforementioned models, so creating direct serializers/APIs for these models is not 
necessary. On top of that, using these models we are creating only user accounts and tokens, no other information is 
is available. If we need detail information about the Manufacturer, Car Dealers, Delivery Agents and Customers, we can 
access respective app/models.py file and retrieve necessary information.

Rather we'll create Registration Serializers/APIs for the aforementioned models. So that we can register respective
users and auto create tokens. 
"""

#-----------------------------------------------------------------------------------------------------------------------

class ManufacturerAccountRegistrationSerializer(serializers.ModelSerializer):

    # necessary field for AbstractUser Model
    password_confirmation = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    # necessary fields for AddressModel
    street = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})
    house = serializers.CharField(max_length=15, required=True, style={'input_type': 'text'})
    zip_code = serializers.CharField(max_length=10, required=True, style={'input_type': 'text'})
    city = serializers.CharField(max_length=200, required=True, style={'input_type': 'text'})
    state = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})
    country = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})

    # necessary fields for Company Model
    name = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})
    registered_on = serializers.DateField(style={'input_type': 'date'}, required=True)
    registration_number = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})

    class Meta:
        model = ManufacturerAccountModel
        fields = ['user_role', 'name', 'street', 'house', 'zip_code', 'city', 'state', 'country', 'registered_on', 'registration_number', 'email', 'username', 'password', 'password_confirmation']
        extra_kwargs = {
            'user_role': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords did not match.'})
        return attrs

    def create(self, validated_data):
        # Creating related address model
        new_address = AddressModel.objects.create(
            street=validated_data['street'],
            house=validated_data['house'],
            zip_code=validated_data['zip_code'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
        )

        # Creating related company model
        new_company = CompanyModel.objects.create(
            name=validated_data['name'],
            address=new_address,
            registered_on=validated_data['registered_on'],
            registration_number=validated_data['registration_number'],
        )

        # Creating related manufacturer model
        new_manufacturer = ManufacturerModel.objects.create(
            company_info=new_company,
        )

        # Creating related user model
        new_user = ManufacturerAccountModel.objects.create(
            user_role=validated_data['user_role'],
            username=validated_data['username'],
            email=validated_data['email'],
            manufacturer_info=new_manufacturer,
        )

        # Hashing the password
        new_user.set_password(validated_data['password'])

        # Saving the complete instance.
        new_user.save()

        return new_user

#-----------------------------------------------------------------------------------------------------------------------

class CarDealerAccountRegistrationSerializer(serializers.ModelSerializer):

    # necessary field for AbstractUser Model
    password_confirmation = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    # necessary fields for AddressModel
    street = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})
    house = serializers.CharField(max_length=15, required=True, style={'input_type': 'text'})
    zip_code = serializers.CharField(max_length=10, required=True, style={'input_type': 'text'})
    city = serializers.CharField(max_length=200, required=True, style={'input_type': 'text'})
    state = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})
    country = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})

    # necessary fields for Company Model
    name = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})
    registered_on = serializers.DateField(style={'input_type': 'date'}, required=True)
    registration_number = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})

    class Meta:
        model = CarDealerAccountModel
        fields = ['user_role', 'name', 'street', 'house', 'zip_code', 'city', 'state', 'country', 'registered_on', 'registration_number', 'email', 'username', 'password', 'password_confirmation']
        extra_kwargs = {
            'user_role': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords did not match.'})
        return attrs

    def create(self, validated_data):
        # Creating related address model
        new_address = AddressModel.objects.create(
            street=validated_data['street'],
            house=validated_data['house'],
            zip_code=validated_data['zip_code'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
        )

        # Creating related company model
        new_company = CompanyModel.objects.create(
            name=validated_data['name'],
            address=new_address,
            registered_on=validated_data['registered_on'],
            registration_number=validated_data['registration_number'],
        )

        # Creating related manufacturer model
        new_car_dealer = CarDealerModel.objects.create(
            company_info=new_company,
        )

        # Creating related user model
        new_user = CarDealerAccountModel.objects.create(
            user_role=validated_data['user_role'],
            username=validated_data['username'],
            email=validated_data['email'],
            car_dealer_info=new_car_dealer,
        )

        # Hashing the password
        new_user.set_password(validated_data['password'])

        # Saving the complete instance.
        new_user.save()

        return new_user

#-----------------------------------------------------------------------------------------------------------------------

class DeliveryAgentAccountRegistrationSerializer(serializers.ModelSerializer):

    # necessary field for AbstractUser Model
    password_confirmation = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    # necessary fields for AddressModel
    street = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})
    house = serializers.CharField(max_length=15, required=True, style={'input_type': 'text'})
    zip_code = serializers.CharField(max_length=10, required=True, style={'input_type': 'text'})
    city = serializers.CharField(max_length=200, required=True, style={'input_type': 'text'})
    state = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})
    country = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})

    # necessary fields for Person Model
    first_name = serializers.CharField(max_length=50, required=True, style={'input_type': 'text'})
    last_name = serializers.CharField(max_length=50, required=True, style={'input_type': 'text'})
    date_of_birth = serializers.DateField(style={'input_type': 'date'}, required=True)
    phone_number = serializers.CharField(max_length=500, required=True, style={'input_type': 'text'})

    class Meta:
        model = DeliveryAgentAccountModel
        fields = ['user_role', 'first_name', 'last_name', 'date_of_birth', 'street', 'house', 'zip_code', 'city', 'state', 'country', 'email', 'phone_number', 'username', 'password', 'password_confirmation']
        extra_kwargs = {
            'user_role': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords did not match.'})
        return attrs

    def create(self, validated_data):
        # Creating related address model
        new_address = AddressModel.objects.create(
            street=validated_data['street'],
            house=validated_data['house'],
            zip_code=validated_data['zip_code'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
        )

        # Creating related person model
        new_person = PersonModel.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            email_address=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=new_address,
        )

        # Creating related delivery agent model
        new_delivery_agent = DeliveryAgentModel.objects.create(
            personal_info=new_person,
        )

        # Creating related user model
        new_user = DeliveryAgentAccountModel.objects.create(
            user_role=validated_data['user_role'],
            username=validated_data['username'],
            email=validated_data['email'],
            delivery_agent_info=new_delivery_agent,
        )

        # Hashing the password
        new_user.set_password(validated_data['password'])

        # Saving the complete instance.
        new_user.save()

        return new_user

#-----------------------------------------------------------------------------------------------------------------------

class CustomerAccountRegistrationSerializer(serializers.ModelSerializer):

    # necessary field for AbstractUser Model
    password_confirmation = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    # necessary fields for AddressModel
    street = serializers.CharField(max_length=100, required=True, style={'input_type': 'text'})
    house = serializers.CharField(max_length=15, required=True, style={'input_type': 'text'})
    zip_code = serializers.CharField(max_length=10, required=True, style={'input_type': 'text'})
    city = serializers.CharField(max_length=200, required=True, style={'input_type': 'text'})
    state = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})
    country = serializers.CharField(max_length=25, required=True, style={'input_type': 'text'})

    # necessary fields for Customer Model
    first_name = serializers.CharField(max_length=50, required=True, style={'input_type': 'text'})
    last_name = serializers.CharField(max_length=50, required=True, style={'input_type': 'text'})
    date_of_birth = serializers.DateField(style={'input_type': 'date'}, required=True)
    phone_number = serializers.CharField(max_length=500, required=True, style={'input_type': 'text'})

    class Meta:
        model = CustomerAccountModel
        fields = ['user_role', 'first_name', 'last_name', 'date_of_birth', 'street', 'house', 'zip_code', 'city', 'state', 'country', 'email', 'phone_number', 'username', 'password', 'password_confirmation']
        extra_kwargs = {
            'user_role': {'required': True},
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords did not match.'})
        return attrs

    def create(self, validated_data):
        # Creating related address model
        new_address = AddressModel.objects.create(
            street=validated_data['street'],
            house=validated_data['house'],
            zip_code=validated_data['zip_code'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
        )

        # Creating related person model
        new_person = PersonModel.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            email_address=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=new_address,
        )

        # Creating related delivery agent model
        new_customer = CustomerModel.objects.create(
            personal_info=new_person,
        )

        # Creating related user model
        new_user = CustomerAccountModel.objects.create(
            user_role=validated_data['user_role'],
            username=validated_data['username'],
            email=validated_data['email'],
            customer_info=new_customer,
        )

        # Hashing the password
        new_user.set_password(validated_data['password'])

        # Saving the complete instance.
        new_user.save()

        return new_user

#-----------------------------------------------------------------------------------------------------------------------
