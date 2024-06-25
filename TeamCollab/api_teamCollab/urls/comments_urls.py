from django.urls import path, include
from api_teamCollab.views.comment_views import CommentView

COMMENT_URLS = [
    path('', CommentView.as_view(), name='comment_list_create'), # all list and create
    path('<int:id>/', CommentView.as_view(), name='comment_details'), # details and delete
    
]