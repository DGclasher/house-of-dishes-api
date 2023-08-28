from .models import *
from .serializers import *
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class RedirectSocial(View):
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        return JsonResponse(json_obj)


class ChefListCreateView(generics.ListCreateAPIView):
    queryset = ChefUser
    serializer_class = ChefAccountSerializer
    permission_classes = []

class ChefLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = ChefLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            data = {
                "access_token": access_token,
                "refresh_token": str(refresh)
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)