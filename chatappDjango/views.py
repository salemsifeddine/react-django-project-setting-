from django.shortcuts import render
from django.http import HttpResponse
from html5lib import serialize
# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *

def home(request):
    return HttpResponse("salem")

class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSer
