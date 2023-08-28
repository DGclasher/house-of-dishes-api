from .models import *
from .serializers import *
from .permissions import *
from users.models import ChefUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ChefListView(generics.ListAPIView):
    queryset = ChefUser.objects.all()
    serializer_class = ChefSerializer

class ChefDishesListView(generics.RetrieveAPIView):
    queryset = ChefUser
    serializer_class = ChefListSerializer
    lookup_field = 'pk'

class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishListCreateView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, IsChef]

class DishUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated, IsChef]

