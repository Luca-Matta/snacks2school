from django.urls import path
from .views import *

urlpatterns = [
    path('user-count/', UserCount.as_view(), name='user-count'),
    path('stores/', StoreList.as_view(), name='store-list'),
    path('csrf-token/', get_csrf_token, name='csrf-token'),
    path('signup/customer/', CustomerSignup.as_view(), name='customer_signup'),
    path('signup/school-staff/', SchoolStaffSignup.as_view(), name='store_signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('provinces/', ProvinceList.as_view(), name='province-list'),
    path('province/schools/', SchoolListByProvince.as_view(), name='school-list-by-province'),
    path('school/classes/', ClassListBySchool.as_view(), name='class-list'),
    path('current-user-data/', CurrentUserData.as_view(), name='current-user-data'),
    path('calendar/week/', WeeklyCalendar.as_view(), name='user_calendar'),
    path('snacks/', SnackList.as_view(), name='snack-list'),
    path('drinks/', DrinkList.as_view(), name='drink-list'),
    path('v1/stripe/stripe-pub-key/', StripeAPIKey.as_view(), name='stripe-key'),
    path('v1/stripe/create-checkout-session/', CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('stripe/webhook/', StripeWebhook.as_view(), name='stripe-webhook'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('delete-order-item/<int:order_id>/<str:item_type>/<int:item_id>/', DeleteOrderItem.as_view(), name='delete-order-item'),
    path('toggle-order-prepared-status/', ToggleOrderPreparedStatus.as_view(), name='toggle-order-prepared-status'),
    path('toggle-order-delivered-status/', ToggleOrderDeliveredStatus.as_view(), name='toggle-order-delivered-status'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders-by-day/', OrdersByDay.as_view(), name='orders-by-day'),
    path('grouped-orders/', OrdersByDateSchoolAndClass.as_view(), name='grouped-orders'),
    path('receipts/', Receipt.as_view(), name='receipts')
]