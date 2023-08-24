from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ChefListCreate(generics.ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes= [TokenAuthentication]

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
