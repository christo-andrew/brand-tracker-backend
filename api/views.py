# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.contrib.auth import authenticate
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from api.models import Place
from api.serializers import PlaceSerializer

logger = logging.getLogger(__name__)


class LoginView(APIView):
    permission_classes = ([])
    authentication_classes = ([])

    @csrf_exempt
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")

        if not (username or password):
            return JsonResponse({"Error": "Username or Password missing"})

        user = authenticate(request, username=username, password=password)

        if not user:
            return JsonResponse({"Message": "Invalid Username/Password", "RESPONSE_CODE": 2001})

        token, created = Token.objects.get_or_create(user=user)

        print token

        return JsonResponse({"token": token.key, "responseCode": 2002})


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
