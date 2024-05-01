from rest_framework import serializers
from .models import Object
from datetime import datetime
from django.utils import timezone

class ObjectSerializer(serializers.ModelSerializer):
    # uploadDateAndTime = serializers.SerializerMethodField()

    # def get_uploadDateAndTime(self, obj):
    #     # Convert the UTC time to the local time zone
    #     local_time = timezone.localtime(obj.uploadDateAndTime)
    #     return local_time


    class Meta:
        model = Object
        fields = '__all__'

    
   