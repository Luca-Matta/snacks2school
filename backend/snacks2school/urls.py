from django.urls import path
from .views import *

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store-list'),
    path('csrf-token/', get_csrf_token, name='csrf-token'),
    path('signup/customer/', CustomerSignup.as_view(), name='customer_signup'),
    path('signup/store/', StoreSignup.as_view(), name='store_signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('current-user-data/', CurrentUserData.as_view(), name='current-user-data'),
    path('user/calendar/', UserCalendar.as_view(), name='user-calendar'),
    path('snacks/', SnackList.as_view(), name='snack-list'),
    path('v1/stripe/stripe-pub-key/', StripeAPIKey.as_view(), name='stripe-key'),
    path('v1/stripe/create-checkout-session/', CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('stripe/webhook/', StripeWebhook.as_view(), name='stripe-webhook'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
]