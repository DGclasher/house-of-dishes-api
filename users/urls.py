from .views import *
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('social/', include('djoser.social.urls')),
    path('accounts/profile/', RedirectSocial.as_view()),    # for testing
    path('chef/', ChefListCreateView.as_view(), name='chef_list_create'),
    path('chef/update/<int:pk>/', ChefUpdateDeleteView.as_view(), name='chef_account_update'),
    path('chef/delete/<int:pk>/', ChefUpdateDeleteView.as_view(), name='chef_account_delete'),
    path('chef/login/', ChefLoginView.as_view(), name='chef_login'),
    # path('api/auth/jwt/create', CustomJWTToken.as_view()),
] 
