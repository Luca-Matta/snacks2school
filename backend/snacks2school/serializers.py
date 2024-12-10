from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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
        model = Snack
        fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Calendar
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    seller = UserSerializer()
    snack = SnackSerializer()

    class Meta:
        model = Order
        fields = '__all__'