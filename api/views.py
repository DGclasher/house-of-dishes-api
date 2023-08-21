from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response

class ChefListCreate(generics.ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class ChefDishesListView(generics.RetrieveAPIView):
    queryset = Chef
    serializer_class = ChefListSerializer
    lookup_field = 'pk'

class ChefUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
