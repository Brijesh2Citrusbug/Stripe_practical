from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


class RegisterView(APIView):
    """
    User register here.
    """
    def post(self, request):
        strip_user = stripe.Customer.create(email=request.data['email'], )
        serializer = RegisterSerializer(data=request.data, context={'customer_id': strip_user['id']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
