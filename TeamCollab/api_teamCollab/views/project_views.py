from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from api_teamCollab.serializers import(
    ProjectSerializer,
)
from api_teamCollab.models import(
    Projects,

)

class ProjectView(APIView):    
    # ======================== Retrive Project Data ==========================
    def get(self, request, id=None, format=None):    
       if id is not None:
            project = Projects.objects.get(id=id)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        
       project = Projects.objects.all()
       serializer = ProjectSerializer(project, many=True)
       return Response(serializer.data)
   

    # ======================== Create Project Data ==========================
    @csrf_exempt   
    def post(self, request, format=None):
        data = request.data
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg_res = {
                'message': 'Project create successfully'
            }
            return Response(msg_res, status=status.HTTP_201_CREATED)
        else:
            msg_res = serializer.errors
            return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)
        
        
    # ======================== Put Project Data ==========================    
    @csrf_exempt    
    def put(self, request, id=None, format=None):
        get_id = id
        if get_id is not None:
            project = Projects.objects.get(pk=get_id)
            data = request.data
            serializer = ProjectSerializer(project, data=data) # all fields
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'Project data complate update successfullly'
                }
                return Response(msg_res, status=status.HTTP_200_OK)
            else:
                msg_res = serializer.errors
                return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)
        else:
            msg_res = {
                'errors': 'Id not found'
            }
            return Response(msg_res, status=status.HTTP_501_NOT_IMPLEMENTED)
        
        
    # ======================== Patch Project Data ==========================    
    @csrf_exempt    
    def patch(self, request, id=None, format=None):
        get_id = id
        if get_id is not None:
            project = Projects.objects.get(pk=get_id)
            data = request.data
            serializer = ProjectSerializer(project, data=data, partial=True) # spacific fileds
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'Project data partial update successfullly'
                }
                return Response(msg_res, status=status.HTTP_200_OK)
            else:
                msg_res = serializer.errors
                return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)
        else:
            msg_res = {
                'errors': 'Id not found'
            }
            return Response(msg_res, status=status.HTTP_501_NOT_IMPLEMENTED)
        
    
    # ======================== Delete Project Data ========================== 
    @csrf_exempt   
    def delete(self, request, id=None):
        get_id = id
        project = Projects.objects.get(pk=get_id)
        if project:
            project.delete()
            msg_res = {
                'message': 'Project delete successfullly'
            }
            return Response(msg_res, status=status.HTTP_200_OK)
        else:
            msg_res = {
                'message': 'Project not found'
            }
            return Response(msg_res, status=status.HTTP_404_NOT_FOUND)
        
        
