from django.contrib.auth.models import User, Group
from rest_framework import serializers

from restaurant.menu.models import Restaurant, Menu, Employee


# serializer for Restaurant model
class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'

    # create method is defined in the Restaurant model
    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    # update method is defined in the Restaurant model
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    # delete method is defined in the Restaurant model
    def delete(self, instance):
        instance.delete()
        return instance

    # get_absolute_url method is defined in the Restaurant model
    def get_absolute_url(self):
        return self.restaurant.get_absolute_url()


# serializer for Menu model
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    # create method is defined in the Restaurant model
    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

    # update method is defined in the Restaurant model
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    # delete method is defined in the Restaurant model
    def delete(self, instance):
        instance.delete()
        return instance

    # get_absolute_url method is defined in the Restaurant model
    def get_absolute_url(self):
        return self.restaurant.get_absolute_url()


# serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    # create method is defined in the Restaurant model
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    # update method is defined in the Restaurant model
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    # delete method is defined in the Restaurant model
    def delete(self, instance):
        instance.delete()
        return instance

    # get_absolute_url method is defined in the Restaurant model
    def get_absolute_url(self):
        return self.restaurant.get_absolute_url()