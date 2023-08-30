from .models import *
from rest_framework import serializers

class CoFounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoFounder
        fields = ("__all__")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("__all__")

class EmployeeMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["employee_id", "first_name", "last_name", "position", "profile_picture"]
