from .views import *
from django.urls import path

urlpatterns = [
    path('chef/', ChefListCreate.as_view(), name='chef_list_create'),
    path('chef/<int:pk>/dishes/', ChefDishesListView.as_view(), name='chef_dishes'),
    path('chef/<int:pk>/', ChefUpdateDeleteView.as_view(), name='chef_update_delete'),
    path('dish/', DishListCreateView.as_view(), name='dish_list_create'),
    path('dish/<int:pk>/', DishUpdateDeleteView.as_view(), name='dish_update_delete')
]
