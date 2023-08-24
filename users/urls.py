from .views import *
from django.urls import path, include

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),
       # Custom JWT implementation. That's optional. It's possible to do this with Djoser settings or just use the default JWT URL
    # path('api/auth/jwt/create', CustomJWTToken.as_view()),

    # REST Implementation of Django Authentication system
    path('', include('djoser.urls')),

    # Djoser Beta extension for social_django
    path('social/', include('djoser.social.urls')),

    # The URL that you could use for testing and that later on can be used for Front-End app Authentication.
    path('accounts/profile/', RedirectSocial.as_view()),

    # The default Djoser endpoints for JWT.
    path('', include('djoser.urls.jwt')),
]