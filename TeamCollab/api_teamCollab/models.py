from django.db import models
from django.contrib.auth.models import User, AbstractUser
from api_teamCollab.constant import USER_ROLE, PRIORITY, STATUS


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email    = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
    
    def __str__(self):
        return str(self.username)
    
    

# ================================== PROJECT MODEL ======================================
class Projects(models.Model):
    name        = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner       = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return str(self.name)
    
# =============================== PROJECT MEMBER MODEL ====================================
class ProjectMembers(models.Model):
    project       = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    project_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    role          = models.CharField(max_length=100, choices=USER_ROLE, null=True, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Project Member'
        verbose_name_plural = 'Project Members'
    
    def __str__(self):
        return str(self.project)
    

# ==================================== TASKS MODEL =======================================
class Tasks(models.Model):
    title       = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status      = models.CharField(max_length=100, choices=STATUS, null=True, blank=True)
    priority    = models.CharField(max_length=100, choices=PRIORITY, null=True, blank=True)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='ts_user', null=True, blank=True)
    project     = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ts_project', null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    due_date    = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return str(self.title)

# ================================== COMMENTS MODEL ======================================
class Comments(models.Model):
    content    = models.TextField(null=True, blank=True)
    user       = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cm_user', null=True, blank=True)
    task       = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='cm_tasks', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return str(self.content)

