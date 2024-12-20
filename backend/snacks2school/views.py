import json
import stripe
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
from decimal import Decimal
import logging
from django.shortcuts import get_object_or_404
from django.db.models import Count, F

logger = logging.getLogger(__name__)
User = get_user_model()


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})


def get_start_of_week():
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    return start_of_week


def get_current_week():
    today = datetime.today().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=5)
    return start_of_week, end_of_week


class ProvinceList(APIView):
    def get(self, request):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SchoolListByProvince(APIView):
    def get(self, request):
        province_id = request.query_params.get('province')
        if province_id:
            schools = School.objects.filter(province_id=province_id)
        else:
            schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ClassList(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerSignup(APIView):
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data.get('email', '')
            password = serializer.validated_data['password']
            first_name = serializer.validated_data.get('first_name', '')
            last_name = serializer.validated_data.get('last_name', '')
            location = serializer.validated_data['location']
            associated_school = serializer.validated_data['associated_school']
            school_class = serializer.validated_data['school_class']

            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if email and User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                location=location,
                associated_school=associated_school,
                school_class=school_class
            )
            
            user.save()

            customer_group, created = Group.objects.get_or_create(name='Customer')
            user.groups.add(customer_group)
            
            token, created = Token.objects.get_or_create(user=user)
            
            start_of_week = get_start_of_week()
            Calendar.objects.create(user=user, week_start_date=start_of_week)
            
            return Response({'token': token.key, 'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreSignup(APIView):
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
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


class CurrentUserData(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CurrentUserDataSerializer(request.user)
        return Response(serializer.data)


class UserCalendar(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        today = datetime.today().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        
        calendar = Calendar.objects.filter(user=user, week_start_date=start_of_week).first()
        
        if calendar:
            week_days = CalendarDay.objects.filter(calendar=calendar, date__range=[start_of_week, end_of_week]).order_by('date')
            data = {
                'week_days': [
                    {
                        'date': day.date,
                        'snacks': [{'name': snack.name} for snack in day.snacks.all()],
                        'drinks': [{'name': drink.name} for drink in day.drinks.all()]
                    }
                    for day in week_days
                ]
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Calendar not found'}, status=status.HTTP_404_NOT_FOUND)
        

class StoreList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        store_group = Group.objects.get(name='Store')
        return User.objects.filter(groups=store_group)


class SnackList(generics.ListAPIView):
    serializer_class = SnackSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            return Snack.objects.filter(seller__username=username).prefetch_related('ingredients')
        return Snack.objects.none()


class DrinkList(generics.ListAPIView):
    serializer_class = SnackSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            return Drink.objects.filter(seller__username=username).prefetch_related('ingredients')
        return Drink.objects.none()
    

class StripeAPIKey(APIView):
    def get(self, request):
        pub_key = settings.STRIPE_PUBLIC_KEY

        return Response({'publicKey': pub_key})
    

class CreateOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        customer = request.user
        seller_id = request.data.get('seller_id')
        snack_id = request.data.get('snack_id')
        drink_id = request.data.get('drink_id')
        delivery_date = request.data.get('selected_date')
        total_price = request.data.get('total_price')
        school_id = request.data.get('school')
        class_id = request.data.get('school_class')
        order_date = datetime.now().date()

        if not seller_id or (not snack_id and not drink_id):
            return Response({'error': 'Seller and at least one of Snack or Drink are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            seller = User.objects.get(id=seller_id)
            snack = Snack.objects.get(id=snack_id) if snack_id else None
            drink = Drink.objects.get(id=drink_id) if drink_id else None
            school = School.objects.get(id=school_id)
            school_class = Class.objects.get(id=class_id)
        except User.DoesNotExist:
            return Response({'error': 'Seller not found'}, status=status.HTTP_404_NOT_FOUND)
        except Snack.DoesNotExist:
            return Response({'error': 'Snack not found'}, status=status.HTTP_404_NOT_FOUND)
        except Drink.DoesNotExist:
            return Response({'error': 'Drink not found'}, status=status.HTTP_404_NOT_FOUND)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        except Class.DoesNotExist:
            return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        calendar, created = Calendar.objects.get_or_create(user=customer, week_start_date=start_of_week)

        calendar_day, created = CalendarDay.objects.get_or_create(calendar=calendar, date=delivery_date)

        if snack:
            calendar_day.snacks.add(snack)
        if drink:
            calendar_day.drinks.add(drink)
        calendar_day.save()

        order = Order(
            customer=customer,
            seller=seller,
            snack=snack,
            drink=drink,
            order_date=order_date,
            delivery_date=delivery_date,
            calendar=calendar,
            school=school,
            school_class=school_class
        )
        order.save()

        total_price_decimal = Decimal(total_price)
        print(total_price_decimal)
        print(customer.credit_wallet_amount)

        if customer.credit_wallet_amount >= total_price_decimal:
            customer.credit_wallet_amount -= total_price_decimal
            customer.save()
        else:
            return Response({'error': 'Insufficient funds in credit wallet'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WeeklyCalendar(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        start_of_week, end_of_week = get_current_week()

        calendar, created = Calendar.objects.get_or_create(
            user=user, week_start_date=start_of_week
        )

        for i in range(6):
            day_date = start_of_week + timedelta(days=i)
            CalendarDay.objects.get_or_create(calendar=calendar, date=day_date)

        delivery_date = request.query_params.get('delivery_date')

        if delivery_date:
            delivery_date = datetime.strptime(delivery_date, '%Y-%m-%d').date()

            CalendarDay.objects.get_or_create(calendar=calendar, date=delivery_date)

        serializer = CalendarSerializer(calendar)
        return Response(serializer.data)


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=5)

        return Order.objects.filter(customer=user, order_date__range=[start_of_week, end_of_week])
    

class OrdersBySchoolAndClass(APIView):
    def get(self, request):
        orders = Order.objects.values(
            'delivery_date', 'school__name', 'school_class__name', 'snack__name', 'drink__name'
        ).annotate(
            snack_count=Count('snack'),
            drink_count=Count('drink')
        ).order_by('delivery_date', 'school__name', 'school_class__name')

        response_data = {}
        for order in orders:
            delivery_date = order['delivery_date'].strftime('%Y-%m-%d')
            school_name = order['school__name']
            class_name = order['school_class__name']
            snack_name = order['snack__name']
            drink_name = order['drink__name']
            snack_count = order['snack_count']
            drink_count = order['drink_count']

            if delivery_date not in response_data:
                response_data[delivery_date] = {}

            if school_name not in response_data[delivery_date]:
                response_data[delivery_date][school_name] = {}

            if class_name not in response_data[delivery_date][school_name]:
                response_data[delivery_date][school_name][class_name] = {'snacks': {}, 'drinks': {}}

            if snack_name:
                if snack_name not in response_data[delivery_date][school_name][class_name]['snacks']:
                    response_data[delivery_date][school_name][class_name]['snacks'][snack_name] = 0
                response_data[delivery_date][school_name][class_name]['snacks'][snack_name] += snack_count

            if drink_name:
                if drink_name not in response_data[delivery_date][school_name][class_name]['drinks']:
                    response_data[delivery_date][school_name][class_name]['drinks'][drink_name] = 0
                response_data[delivery_date][school_name][class_name]['drinks'][drink_name] += drink_count

        return Response(response_data, status=status.HTTP_200_OK)    


class CreateCheckoutSession(APIView):
    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price_id = settings.STRIPE_PRICE_ID_WALLET_CHARGE

        print('Creating checkout session for user:', request.user.id)

        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=str(request.user.id),
                success_url='%s?session_id={CHECKOUT_SESSION_ID}' % settings.FRONTEND_WEBSITE_SUCCESS_URL,
                cancel_url='%s' % settings.FRONTEND_WEBSITE_CANCEL_URL,
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1
                    }
                ]
            )
            print('Checkout session created with session ID:', checkout_session['id'])
            print('Client reference ID:', checkout_session['client_reference_id'])

            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            print('Error creating checkout session:', str(e))
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhook(APIView):
    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        webhook_key = settings.STRIPE_WEBHOOK_KEY
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_key
            )
        except ValueError as e:
            logger.error('Invalid payload: %s', e)
            print('Invalid payload:', e)
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            logger.error('Invalid signature: %s', e)
            print('Invalid signature:', e)
            return HttpResponse(status=400)
        
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            customer_id = session.get('client_reference_id')
            logger.info('customer_id: %s', customer_id)
            print('customer_id:', customer_id)
            if customer_id is None:
                logger.error('No customer_id found in session')
                print('No customer_id found in session')
                return HttpResponse(status=400)
            try:
                customer = User.objects.get(id=customer_id)
                logger.info('Customer found: %s', customer)
                print('Customer found:', customer)
                customer.credit_wallet_amount += 20
                customer.save()
                logger.info('Customer wallet updated')
                print('Customer wallet updated')
                return HttpResponse(status=200)
            except User.DoesNotExist:
                logger.error('Customer does not exist')
                print('Customer does not exist')
                return HttpResponse(status=404)
            except Exception as e:
                logger.error('Error updating customer wallet: %s', e)
                print('Error updating customer wallet:', e)
                return HttpResponse(status=500)

        return HttpResponse(status=200)