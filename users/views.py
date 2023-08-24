from .serializers import *
from django.views import View
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth.models import User

class RedirectSocial(View):
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        return JsonResponse(json_obj)

