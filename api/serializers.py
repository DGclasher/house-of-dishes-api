from .models import *
from rest_framework import serializers


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class DishMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id','name']

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['id', 'name', 'email']

class ChefListSerializer(serializers.ModelSerializer):
    dishes = serializers.SerializerMethodField()
    class Meta:
        model = Chef
        fields = ['id', 'name', 'email', 'dishes']
    def get_dishes(self, obj):
        dishes = Dish.objects.filter(chef=obj)
        return DishMinimalSerializer(dishes, many=True).data