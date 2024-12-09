from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import date, timedelta

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    store_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=70, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='snacks2school_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='snacks2school_user_set', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    credit_wallet_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stripe_customer_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_or_create_current_week_calendar(self):
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        
        calendar, created = Calendar.objects.get_or_create(user=self, week_start_date=start_of_week)
        return calendar
    

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendars', null=True, blank=True)
    week_start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Calendar for {self.user.username} starting {self.week_start_date}"

    def get_week_days(self):
        if self.week_start_date is None:
            return []
        start_of_week = self.week_start_date - timedelta(days=self.week_start_date.weekday())
        return [start_of_week + timedelta(days=i) for i in range(7)]

    def get_snacks_for_week(self):
        week_days = self.get_week_days()
        snacks_by_day = {day: Snack.objects.filter(date=day, seller=self.user) for day in week_days}
        return snacks_by_day
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ingredient_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snacks', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='snack_images/', null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='snacks', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_customer', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_seller', null=True, blank=True)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE, null=True, blank=True)
    snack_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order by {self.customer.username} from {self.seller.username} for {self.snack.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.customer and self.order_date:
            start_of_week = self.order_date - timedelta(days=self.order_date.weekday())
            calendar = Calendar.objects.filter(user=self.customer, week_start_date=start_of_week).first()
            if calendar:
                self.snack.date = self.order_date
                self.snack.seller = self.seller
                self.snack.save()
                calendar_snacks = calendar.get_snacks_for_week()
                if self.order_date in calendar_snacks:
                    calendar_snacks[self.order_date].append(self.snack)
                else:
                    calendar_snacks[self.order_date] = [self.snack]
                calendar.save()