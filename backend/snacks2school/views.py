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
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
User = get_user_model()


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})


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
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CurrentUserDataSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserCalendar(APIView):

    def get(self, request):
        user = request.user
        if user.is_anonymous:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

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


class SnackList(generics.ListAPIView):
    serializer_class = SnackSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            return Snack.objects.filter(seller__username=username).prefetch_related('ingredients')
        return Snack.objects.none()
    

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
    

class CreateCheckoutSession(APIView):
    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price_id = settings.STRIPE_PRICE_ID_WALLET_CHARGE

        # Debugging: Print user ID
        print('Creating checkout session for user:', request.user.id)

        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=str(request.user.id),
                # success_url=settings.FRONTEND_WEBSITE_SUCCESS_URL,
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
            # Debugging: Print session ID and client reference ID
            print('Checkout session created with session ID:', checkout_session['id'])
            print('Client reference ID:', checkout_session['client_reference_id'])

            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            # Debugging: Print error
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