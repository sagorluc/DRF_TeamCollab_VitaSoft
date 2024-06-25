from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from api_teamCollab.serializers import(
    CommentSerializer,
    TaskSerializer
)
from api_teamCollab.models import(
    Comments,
    Tasks
)

class CommentView(APIView):
    
    # ======================== Retrive Comment Data ==========================
    def get(self, request, id=None, task_id=None):      
        if id:
           try:
                comment = Comments.objects.get(id=id)
                serializer = CommentSerializer(comment)
                return Response(serializer.data)
           except Comments.DoesNotExist:
               return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
           
        if task_id:
           try:
                task = Tasks.objects.get(pk=task_id)
                comments = Comments.objects.filter(task=task)
           except Tasks.DoesNotExist:
               return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            comments = Comments.objects.all()
        
        serializer = CommentSerializer(comments, many=True) 
        return Response(serializer.data)

    # ======================== Create Comment Data ==========================
    @csrf_exempt   
    def post(self, request, task_id=None):
        data = request.data
        try:
            task = Tasks.objects.get(pk=task_id)
        except Tasks.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(task=task)
            msg_res = {
                'message': 'Comment create successfully'
            }
            return Response(msg_res, status=status.HTTP_201_CREATED)
        else:
            msg_res = serializer.errors
            return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)
    
    # ========================== Put Comment Data ===========================    
    @csrf_exempt    
    def put(self, request, id=None):
        try:
            comment = Comments.objects.get(pk=id)
        except Comments.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = CommentSerializer(comment, data=data) # all fields
        if serializer.is_valid():
            serializer.save()
            msg_res = {
                'message': 'Comment data complate update successfullly'
            }
            return Response(msg_res, status=status.HTTP_200_OK)
        else:
            msg_res = serializer.errors
            return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)

        
    
    # ========================== Patch Comment Data ============================    
    @csrf_exempt    
    def patch(self, request, id=None):
        if id is not None:
            comment = Comments.objects.get(pk=id)
            data = request.data
            serializer = CommentSerializer(comment, data=data, partial=True) # spacific fileds
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'Comment data partial update successfullly'
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
    
    
    # ========================== Delete Comment Data ============================ 
    @csrf_exempt   
    def delete(self, request, id=None):
        comment = Comments.objects.get(pk=id)
        if comment:
            comment.delete()
            msg_res = {
                'message': 'Comment delete successfullly'
            }
            return Response(msg_res, status=status.HTTP_200_OK)
        else:
            msg_res = {
                'message': 'Comment not found'
            }
            return Response(msg_res, status=status.HTTP_404_NOT_FOUND)
        
        
