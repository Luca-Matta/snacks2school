from django.urls import path
from .views import UserList, Login, get_csrf_token

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('csrf-token/', get_csrf_token, name='csrf-token'),
    path('login/', Login.as_view(), name='login'),
]