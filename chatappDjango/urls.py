from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',RoomView.as_view()),
     
]
