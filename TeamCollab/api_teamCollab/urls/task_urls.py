from django.urls import path, include
from api_teamCollab.views.task_views import TaskView
from api_teamCollab.views.comment_views import CommentView

TASK_URLS = [
    path('', TaskView.as_view()), 
    path('<int:id>/', TaskView.as_view(), name='task_details'),
    path('<int:task_id>/comments/', CommentView.as_view(), name='comment_list_create'),
    
]