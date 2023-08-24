from .serializers import *
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

class RedirectSocial(View):
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        return JsonResponse(json_obj)


