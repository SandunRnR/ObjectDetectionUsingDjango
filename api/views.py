from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ObjectSerializer
from .models import Object
from rest_framework import status
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/object-list/',
        'Detail View': 'object-detail/<int:id>',
        'Create': '/object-create/',
        'Update': '/object-update/',
        'Delete': '/object-detail<int:id>',
    }
    return Response(api_urls);


@api_view(['POST'])
def CreateObject(request):
    if request.method == 'POST':
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will automatically set the uploadDateAndTime field
            # Return a response with only the necessary fields (id and name)
            return Response({"id": serializer.instance.id, "name": serializer.instance.name,"uploadDateAndTime":datetime.now()}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
