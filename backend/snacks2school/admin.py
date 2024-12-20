from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('location', 'address', 'profile_picture', 'bio', 'store_name', 'credit_wallet_amount', 'stripe_customer_id', 'associated_school', 'school_class')}),
    )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)


class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'seller', 'net_price', 'gross_price')
    search_fields = ('name', 'seller__username')
    readonly_fields = ('gross_price',)


class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'seller', 'net_price', 'gross_price')
    search_fields = ('name', 'seller__username')
    readonly_fields = ('gross_price',)


class CalendarDayAdmin(admin.ModelAdmin):
    list_display = ('calendar', 'date')
    search_fields = ('calendar__user__username', 'date')


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'week_start_date')
    search_fields = ('user__username',)
    readonly_fields = ('display_snacks_for_week', 'display_drinks_for_week')

    def display_snacks_for_week(self, obj):
        snacks_by_day = obj.get_snacks_for_week()
        result = ""
        for day, snacks in snacks_by_day.items():
            result += f"{day}:\n"
            for snack in snacks:
                result += f"  - {snack.name} (Seller: {snack.seller.username})\n"
        return result

    def display_drinks_for_week(self, obj):
        drinks_by_day = obj.get_drinks_for_week()
        result = ""
        for day, drinks in drinks_by_day.items():
            result += f"{day}:\n"
            for drink in drinks:
                result += f"  - {drink.name} (Seller: {drink.seller.username})\n"
        return result

    display_snacks_for_week.short_description = 'Snacks for the Week'
    display_drinks_for_week.short_description = 'Drinks for the Week'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'seller', 'snack', 'drink', 'order_date', 'get_store_name')
    search_fields = ('customer__username', 'seller__username', 'snack__name', 'drink__name', 'seller__store_name')

    def get_store_name(self, obj):
        return obj.seller.store_name
    get_store_name.short_description = 'Store Name'


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def get_school_name(self, obj):
        return obj.school.name or "Unnamed School"
    get_school_name.short_description = 'School Name'

admin.site.register(User, CustomUserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Snack, SnackAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(CalendarDay, CalendarDayAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Class, ClassAdmin)