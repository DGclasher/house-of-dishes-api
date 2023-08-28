from .views import *
from django.urls import path, include

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('social/', include('djoser.social.urls')),
    path('accounts/profile/', RedirectSocial.as_view()),    # for testing
    path('chef/', ChefListCreateView.as_view(), name='chef_list_create'),
    path('chef/login/', ChefLoginView.as_view(), name='chef_login'),
    # path('api/auth/jwt/create', CustomJWTToken.as_view()),
]