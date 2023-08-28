from .models import *
from .serializers import *
from rest_framework import generics

class CoFounderListView(generics.ListAPIView):
    queryset = CoFounders.objects.all()
    serializer_class = CoFounderSerializer
    permission_classes = []

class EmployeeListAllView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeMinimalSerializer
    permission_classes = []

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = []
    lookup_field = 'employee_id'
    