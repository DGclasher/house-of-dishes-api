from .views import *
from django.urls import path

urlpatterns = [
    path('dish/', DishListView.as_view(), name='dish_list'),
    path('dish/filter/<int:id>/id/', DishByIdView.as_view(), name='dish_by_id'),
    path('dish/filter/state/' , DishListState.as_view() , name='dish_by_state'),
    path('dish/filter/course/' ,DishListCourse.as_view() , name="dish_list_course" ),
    path('dish/filter/choice/' ,DishListChoice.as_view() , name="dish_list_choice" ),
    path('dish/filter/ingredients/' ,DishListIngredients.as_view() , name="dish_list_ingredients" ),
    path('dish/filter/search/', DishSearchView.as_view(), name="search_dish"),

    path('dish/create/', DishListCreateView.as_view(), name='dish_create'),
    path('dish/<int:pk>/chef', DishUpdateDeleteView.as_view(), name='dish_update_delete'),
    path('chef/', ChefListView.as_view(), name='chef_list_create'),
    path('chef/<int:pk>/dishes/', ChefDishesListView.as_view(), name='chef_dishes'),

    path('contact/', ContactView.as_view(), name='contact'),
]
