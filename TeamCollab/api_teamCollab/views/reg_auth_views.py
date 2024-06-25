from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from api_teamCollab.serializers import(
    CustomUserSerializer,
)
from api_teamCollab.models import(
    CustomUser,
)

class RegistrationView(APIView):
    # ========================== Retrive User Data ============================
    def get(self, request, id=None):      
       if id:
           try:
                user = CustomUser.objects.get(id=id)
                serializer = CustomUserSerializer(user)
                return Response(serializer.data)
           except CustomUser.DoesNotExist:
               return Response('Custom user not found', status=status.HTTP_400_BAD_REQUEST)
        
       users = CustomUser.objects.all()
       serializer = CustomUserSerializer(users, many=True)
       return Response(serializer.data)

    
     # ========================== Create User Data ============================
    @csrf_exempt   
    def post(self, request):
        data = request.data
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(username=data['username'])
            token = Token.objects.get(user=user)
            serializer = CustomUserSerializer(user)
            
            msg_res = {
                'message': 'User create successfully',
                'user': serializer.data,
                'token': token.key,
            }
            return Response(msg_res, status=status.HTTP_201_CREATED)
        else:
            msg_res = serializer.errors
            return Response(msg_res, status=status.HTTP_400_BAD_REQUEST)
        
    
     # ========================== Put User Data ============================    
    @csrf_exempt    
    def put(self, request, id=None):
        get_id = id
        if get_id is not None:
            user = CustomUser.objects.get(pk=get_id)
            data = request.data
            serializer = CustomUserSerializer(user, data=data) # all fields
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'User data complate update successfullly'
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
        
        
     # ========================== Patch User Data ============================    
    @csrf_exempt    
    def patch(self, request, id=None):
        get_id = id
        if get_id is not None:
            user = CustomUser.objects.get(pk=get_id)
            data = request.data
            serializer = CustomUserSerializer(user, data=data, partial=True) # spacific fileds
            if serializer.is_valid():
                serializer.save()
                msg_res = {
                    'message': 'User data partial update successfullly'
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
    
    
     # =========================== Delete User Data ============================ 
    @csrf_exempt   
    def delete(self, request, id=None):
        get_id = id
        user = CustomUser.objects.get(pk=get_id)
        if user:
            user.delete()
            msg_res = {
                'message': 'User delete successfullly'
            }
            return Response(msg_res, status=status.HTTP_200_OK)
        else:
            msg_res = {
                'message': 'User not found'
            }
            return Response(msg_res, status=status.HTTP_404_NOT_FOUND)
        
        
class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return Response({'msg': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            user = CustomUser.objects.get(username=username)
            serializer = CustomUserSerializer(user)
            msg_res = {
                'message': 'Login successfully',
                'user': serializer.data,
            }
            token, created = Token.objects.get_or_create(user=user)
            msg_res['token'] = token.key

            return Response(msg_res, status=status.HTTP_200_OK)
        return Response({'msg': 'User not authorized'}, status=status.HTTP_400_BAD_REQUEST)
