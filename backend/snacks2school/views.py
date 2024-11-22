from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta

User = get_user_model()

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

class CustomerSignupView(APIView):
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data.get('email', '')
            password = serializer.validated_data['password']
            first_name = serializer.validated_data.get('first_name', '')
            last_name = serializer.validated_data.get('last_name', '')
            location = serializer.validated_data['location']

            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if email and User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, location=location)
            
            customer_group, created = Group.objects.get_or_create(name='Customer')
            user.groups.add(customer_group)
            
            token, created = Token.objects.get_or_create(user=user)
            
            start_of_week = get_start_of_week()
            Calendar.objects.create(user=user, week_start_date=start_of_week)
            
            return Response({'token': token.key, 'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreSignupView(APIView):
    def post(self, request):
        serializer = StoreSignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data.get('email', '')
            password = serializer.validated_data['password']
            store_name = serializer.validated_data['store_name']
            location = serializer.validated_data['location']

            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if email and User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, email=email, password=password, store_name=store_name, location=location)
            
            store_group, created = Group.objects.get_or_create(name='Store')
            user.groups.add(store_group)
            
            token, created = Token.objects.get_or_create(user=user)
            
            start_of_week = get_start_of_week()
            Calendar.objects.create(user=user, week_start_date=start_of_week)
            
            return Response({'token': token.key, 'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                print("Authentication failed for user:", username)
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            print("Invalid data:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class CurrentUserData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CurrentUserDataSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCalendarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = datetime.today().date()
        start_of_week = today - timedelta(days=today.weekday())
        calendar = Calendar.objects.filter(user=user, week_start_date=start_of_week).first()
        
        if calendar:
            serializer = CalendarSerializer(calendar)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Calendar not found'}, status=status.HTTP_404_NOT_FOUND)
        
class StoreList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        store_group = Group.objects.get(name='Store')
        return User.objects.filter(groups=store_group)
        
class SnackListView(generics.ListAPIView):
    serializer_class = SnackSerializer

    def get_queryset(self):
        store_id = self.request.query_params.get('store_id')
        if store_id:
            return Snack.objects.filter(seller_id=store_id)
        return Snack.objects.none()
    
class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        customer = request.user
        seller_id = request.data.get('seller_id')
        snack_id = request.data.get('snack_id')
        order_date = datetime.now().date()

        if not seller_id or not snack_id:
            return Response({'error': 'Seller and Snack are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            seller = User.objects.get(id=seller_id)
            snack = Snack.objects.get(id=snack_id)
        except User.DoesNotExist:
            return Response({'error': 'Seller not found'}, status=status.HTTP_404_NOT_FOUND)
        except Snack.DoesNotExist:
            return Response({'error': 'Snack not found'}, status=status.HTTP_404_NOT_FOUND)

        order = Order(customer=customer, seller=seller, snack=snack, order_date=order_date)
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)