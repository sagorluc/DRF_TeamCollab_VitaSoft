from django.contrib import admin
from django.contrib.auth.models import User
from api_teamCollab.models import(
    CustomUser,
    Projects,
    ProjectMembers,
    Tasks,
    Comments,
)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    ordering = ['-id']
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner']
    ordering = ['-id']
    
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'project_owner', 'role']
    ordering = ['-id']
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'priority', 'assigned_to', 'project']
    ordering = ['-id']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'task']
    ordering = ['-id']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(ProjectMembers, ProjectMemberAdmin)
admin.site.register(Tasks, TaskAdmin)
admin.site.register(Comments, CommentAdmin)
