from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
        

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']


class BaseSignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False, allow_blank=True)
    location = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Le password non corrispondono.")
        return data


class CustomerSignupSerializer(BaseSignupSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    location = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all(), required=True)
    associated_school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=True)
    school_class = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'location', 'associated_school', 'school_class']


class StoreSignupSerializer(BaseSignupSerializer):
    store_name = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class CurrentUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'image']


class SnackSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Snack
        fields = '__all__'


class DrinkSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Drink
        fields = '__all__'


class CalendarDaySerializer(serializers.ModelSerializer):
    snacks = SnackSerializer(many=True)
    drinks = DrinkSerializer(many=True)

    class Meta:
        model = CalendarDay
        fields = ['date', 'snacks', 'drinks']


class CalendarSerializer(serializers.ModelSerializer):
    days = CalendarDaySerializer(many=True, source='days.all')

    class Meta:
        model = Calendar
        fields = ['week_start_date', 'days']


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    seller = UserSerializer()
    snack = SnackSerializer()
    drink = DrinkSerializer()

    class Meta:
        model = Order
        fields = '__all__'