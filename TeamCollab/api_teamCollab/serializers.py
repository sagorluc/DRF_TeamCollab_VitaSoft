from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from api_teamCollab.models import(
    CustomUser,
    Projects,
    ProjectMembers,
    Tasks,
    Comments,
)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'description', 'owner']
        


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembers
        fields = ['project', 'project_owner', 'role']
        


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'status', 'priority', 'assigned_to', 'project']
        


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['content', 'user', 'task']
        

