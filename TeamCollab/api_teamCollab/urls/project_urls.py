from django.urls import path, include
from api_teamCollab.views.project_views import ProjectView
from api_teamCollab.views.task_views import TaskView

PROJECT_URLS = [
    path('', ProjectView.as_view(), name='project_list_create'),
    path('<int:id>/', ProjectView.as_view(), name='project_details'),
    path('<int:project_id>/tasks/', TaskView.as_view(), name='task_list_create'),
    
    
]