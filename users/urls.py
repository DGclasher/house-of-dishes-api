from .views import *
from django.urls import path, include

urlpatterns = [
    # path('api/auth/jwt/create', CustomJWTToken.as_view()),
    # REST Implementation of Django Authentication system
    path('', include('djoser.urls')),
    path('social/', include('djoser.social.urls')),
    path('accounts/profile/', RedirectSocial.as_view()),

    path('', include('djoser.urls.jwt')),
]