from pyexpat import model
from rest_framework import serializers
from .models import * 

class RoomSer(serializers.ModelSerializer):
    class Meta:
        model=Room 
        fields= "__all__"