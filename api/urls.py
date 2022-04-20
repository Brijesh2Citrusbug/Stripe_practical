from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('plan/', PlanView.as_view(), name='plan'),

]