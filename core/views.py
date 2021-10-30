from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.conf import settings
from django.db import IntegrityError
import requests


def homeView (request,*args, **kwargs):
	return render(request, 'index.html')

class RegisterUser(APIView):
    def post(self,request,*args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        is_doctor = request.data.get('occupation') == "doctor"

        if password1 != password2:
            return Response({"Your password1 and password2 didn't match"},status=status.HTTP_400_BAD_REQUEST)

        else:
            if len(password1) < 8:
                return Response({"Your password must be atleast 8 characters long"},status=status.HTTP_400_BAD_REQUEST)
            
            try:
                user = User.objects.create_user(username, email, password1)
                # for deployed url
                uri = 'https://palliativecare.herokuapp.com/api/token/'

                if settings.DEBUG:
                    uri = 'http://localhost:8000/api/token/'

                http_method='POST'
                body = {
                    "Content-Type" : "application/json",
                    'username': username,
                    'password': password1,
                }
                # newrequest = Request(uri=uri,http_method=http_method,body=body)
                user.save()
                newreq = requests.post(uri,body)
                return Response(newreq.json(),status= status.HTTP_201_CREATED)
            
            except IntegrityError:
                return Response({'Username Already Exists. Please Try New Username'},status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                # print(e.__class__.__name__)
                return Response({"Unknown Error Occured. Please Try Later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# for checking either the user with particular username or email exists or not
class CheckUser(APIView):
    def get(self,request,*args,**kwargs):
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        
        if email == '':    # for checking username
            if User.objects.filter(username = username).exists():
                return Response({'True'},status=status.HTTP_200_OK)
            else:
                return Response({"False"},status = status.HTTP_200_OK)

        else:   # for checking email
            if User.objects.filter(email = email).exists():
                return Response({'True'},status=status.HTTP_200_OK)
            else:
                return Response({"False"},status = status.HTTP_200_OK)
