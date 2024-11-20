from django.urls import path
from .views import *

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store-list'),
    path('csrf-token/', get_csrf_token, name='csrf-token'),
    path('signup/customer/', CustomerSignupView.as_view(), name='customer_signup'),
    path('signup/store/', StoreSignupView.as_view(), name='store_signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('current-user-data/', CurrentUserData.as_view(), name='current-user-data'),
]