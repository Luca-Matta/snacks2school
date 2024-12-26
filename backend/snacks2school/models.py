from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import date, timedelta
from decimal import Decimal

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    store_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
    location = models.ForeignKey('Province', on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='snacks2school_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='snacks2school_user_set', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    credit_wallet_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=255, null=True, blank=True)
    associated_school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    school_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_or_create_current_week_calendar(self):
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        
        calendar, created = Calendar.objects.get_or_create(user=self, week_start_date=start_of_week)
        return calendar
    

class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class School(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed School"
    

class Class(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Calendar(models.Model):
    week_start_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Calendar for week starting {self.week_start_date}"


class CalendarDay(models.Model):
    calendar = models.ForeignKey(Calendar, related_name='days', on_delete=models.CASCADE)
    date = models.DateField()
    snacks = models.ManyToManyField('Snack', blank=True)
    drinks = models.ManyToManyField('Drink', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['calendar', 'date']),
        ]

    def __str__(self):
        return f"{self.date} - {self.calendar.user.username}"

    def get_snacks(self):
        return self.snacks.all()

    def get_drinks(self):
        return self.drinks.all()
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ingredient_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snack_seller', null=True, blank=True)
    net_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gross_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='snack_images/', null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='snack_ingredients', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.net_price is not None:
            self.gross_price = self.net_price * Decimal('1.15')
        super().save(*args, **kwargs)


class Drink(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drink_seller', null=True, blank=True)
    net_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gross_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='snack_images/', null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='drink_ingredients', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.net_price is not None:
            self.gross_price = self.net_price * Decimal('1.15')
        super().save(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_customer', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_seller', null=True, blank=True)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE, null=True, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True, blank=True)
    snack_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    drink_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    school_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    prepared = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        customer_name = self.customer.username if self.customer else 'Unknown customer'
        seller_name = self.seller.username if self.seller else 'Unknown seller'
        snack_name = self.snack.name if self.snack else 'No snack'
        drink_name = self.drink.name if self.drink else 'No drink'
        return f"Order by {customer_name} from {seller_name} for {snack_name} and {drink_name}"
    
    def save(self, *args, **kwargs):
        if self.snack and self.drink:
            self.snack_price = self.snack.gross_price
            self.drink_price = self.drink.gross_price
            self.total_price = self.snack_price + self.drink_price
        super().save(*args, **kwargs)