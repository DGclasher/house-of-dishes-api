from .views import *
from django.urls import path

urlpatterns = [
    path('dish/', DishListView.as_view(), name='dish_list'),
    path('dish/create/', DishListCreateView.as_view(), name='dish_create'),
    path('dish/<int:pk>/', DishUpdateDeleteView.as_view(), name='dish_update_delete'),
    path('chef/', ChefListView.as_view(), name='chef_list_create'),
    path('chef/<int:pk>/dishes/', ChefDishesListView.as_view(), name='chef_dishes'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('dishstate/<str:state_slug>/' , DishListState.as_view() , name='dish_by_state')
]
