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

#Send Details to the Database
@api_view(['POST'])
def CreateObject(request):
    if request.method == 'POST':
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will automatically set the uploadDateAndTime field
            # Return a response with only the necessary fields (id and name)
            return Response({"id": serializer.instance.id, "class_name": serializer.instance.class_name, "confidence": serializer.instance.confidence, "timestamp": datetime.now()}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Get All Details from the database 
@api_view(['GET'])
def GetAllObjects(request):
    if request.method == 'GET':
        # Retrieve all objects from the database
        objects = Object.objects.all()
        
        # Serialize the objects
        serializer = ObjectSerializer(objects, many=True)
        
        # Return a response with serialized data
        return Response(serializer.data)
    
#Get Details using Id
@api_view(['GET'])
def GetObjectById(request, id):
    try:
        # Retrieve object by ID from the database
        obj = Object.objects.get(pk=id)
    except Object.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Serialize the object
    serializer = ObjectSerializer(obj)
    
    # Return a response with serialized data
    return Response(serializer.data)