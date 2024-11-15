from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('csrf-token/', get_csrf_token, name='csrf-token'),
    path('login/', Login.as_view(), name='login'),
    path('current-user-data/', CurrentUserData.as_view(), name='current-user-data'),
]