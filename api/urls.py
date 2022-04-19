from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]