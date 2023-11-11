from .models import *
from .serializers import *
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group
class RedirectSocial(View):
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        return JsonResponse(json_obj)

class ChefListCreateView(generics.ListCreateAPIView):
    queryset = ChefUser.objects.all()
    serializer_class = ChefAccountSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = ChefAccountSerializer(data=request.data)
        if serializer.is_valid():
            chef = serializer.save()
            refresh = RefreshToken.for_user(chef)
            access = str(refresh.access_token)
            data = {
                "account_id":chef.id,
                "email":chef.email,
                "first_name":chef.first_name,
                "access_token":access,
                "refresh_token":str(refresh)
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class ChefRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChefUser.objects.all()
    serializer_class = ChefAccountSerializer

    def get_object(self):
        return self.request.user

class ChefLoginView(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = ChefLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            data = {
                "account_id":user.id,
                "email":user.email,
                "first_name":user.first_name,
                "access_token": access_token,
                "refresh_token": str(refresh)
            }
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"message":"Unable to login with given credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class RequestPasswordReset(generics.GenericAPIView):
    serializer_class = RequestPasswordResetSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = RequestPasswordResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pass
        pass

class GraphicListCreateView(generics.ListCreateAPIView):
    queryset = GraphicUser.objects.all()
    serializer_class = GraphicUserSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = GraphicUserSerializer(data=request.data)
        if serializer.is_valid():
            Graphic = serializer.save()
            refresh = RefreshToken.for_user(Graphic)
            access = str(refresh.access_token)
            print(Graphic)
            data = {
                "account_id": Graphic.id,
                "email": Graphic.email,
                "first_name": Graphic.first_name,
                "access_token": access,
                "refresh_token": str(refresh)
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class GraphicLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = GraphicLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            data = {
                "account_id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "access_token": access_token,
                "refresh_token": str(refresh)
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({"message": "Unable to login with given credentials."}, status=status.HTTP_401_UNAUTHORIZED)