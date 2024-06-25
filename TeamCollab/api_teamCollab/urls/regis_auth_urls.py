from django.urls import path, include
from api_teamCollab.views.reg_auth_views import RegistrationView, LoginView

REGISTRATION_URLS = [
    path('', RegistrationView.as_view(), name='user_list'), # list of all users
    path('register/', RegistrationView.as_view(), name='register'),
    path('<int:id>/', RegistrationView.as_view(), name='register_user_details'),
    path('login/', LoginView.as_view(), name='login'),
]