from django.urls import path, include
from api_teamCollab.urls.regis_auth_urls import REGISTRATION_URLS 
from api_teamCollab.urls.project_urls import PROJECT_URLS
from api_teamCollab.urls.task_urls import TASK_URLS
from api_teamCollab.urls.comments_urls import COMMENT_URLS

urlpatterns = [
    path('api/users/', include(REGISTRATION_URLS)),
    path('api/projects/', include(PROJECT_URLS)),
    path('api/tasks/', include(TASK_URLS)),
    path('api/comments/', include(COMMENT_URLS)),
    
]