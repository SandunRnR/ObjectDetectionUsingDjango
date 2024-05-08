from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Object
from rest_framework import status
from datetime import datetime
from .serializers import ObjectSerializer
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@api_view(['POST'])
def create_object(request):
    if request.method == 'POST':
        # Assuming you are passing 'class_name' and 'confidence' in the request data
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
    if request.method == 'GET':
        try:
            # Retrieve object by ID from the database
            obj = Object.objects.get(pk=id)
        except Object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the object
        serializer = ObjectSerializer(obj)
        
        # Return a response with serialized data
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_object_by_id(request, object_id):
    if request.method == 'DELETE':
        try:
            # Retrieve the object by its ID
            obj = Object.objects.get(pk=object_id)
            
            # Delete the object
            obj.delete()
            
            return Response({"message": f"Object with id {object_id} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Object.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['PUT'])
def update_object_by_id(request, object_id):
    if request.method == 'PUT':
        try:
            # Retrieve the object by its ID
            obj = Object.objects.get(pk=object_id)
            
            # Deserialize the updated data
            serializer = ObjectSerializer(obj, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  # Save the updated object
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Object.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)