from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from api_teamCollab.serializers import(
    TaskSerializer,
    ProjectSerializer

)
from api_teamCollab.models import(
    Tasks,
    Projects

)

class TaskView(APIView):
    
     # =========================== Retrive Task Data ==============================
    def get(self, request, id=None, project_id=None):
        if id:
            try:
                task = Tasks.objects.get(id=id)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except Tasks.DoesNotExist:
                return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if project_id:
            try:
                project = Projects.objects.get(id=project_id)
                tasks = Tasks.objects.filter(project=project) # filtering task according to project
            except Projects.DoesNotExist:
                return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = Tasks.objects.all()
        
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    
     # =========================== Create Task Data ==============================
    @csrf_exempt   
    def post(self, request, project_id=None):
        try:
            project = Projects.objects.get(id=project_id)
        except Projects.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project=project)
            msg_res = {
                'message': 'Task create successfully'
            }
            return Response(msg_res, status=status.HTTP_201_CREATED)
        else:
            msg_res = serializer.errors
            return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)
    
     # =========================== Put Task Data ==============================    
    @csrf_exempt    
    def put(self, request, id=None):
        if id is not None:
            task = Tasks.objects.get(pk=id)
            data = request.data
            serializer = TaskSerializer(task, data=data) # all fields
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'Task data complate update successfullly'
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
        
    
     # =========================== Patch Task Data ==============================    
    @csrf_exempt    
    def patch(self, request, id=None):
        if id is not None:
            task = Tasks.objects.get(pk=id)
            data = request.data
            serializer = TaskSerializer(task, data=data, partial=True) # spacific fileds
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'Task data partial update successfullly'
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
    
    
     # =========================== Delete Task Data ============================== 
    @csrf_exempt   
    def delete(self, request, id=None):
        task = Tasks.objects.get(pk=id)
        if task:
            task.delete()
            msg_res = {
                'message': 'Task delete successfullly'
            }
            return Response(msg_res, status=status.HTTP_200_OK)
        else:
            msg_res = {
                'message': 'Task not found'
            }
            return Response(msg_res, status=status.HTTP_404_NOT_FOUND)
        
        
