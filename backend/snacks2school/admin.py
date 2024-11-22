from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Snack, Calendar, Order

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('location', 'profile_picture', 'bio', 'store_name')}),
    )

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'seller')
    search_fields = ('name', 'seller__username')

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'week_start_date')
    search_fields = ('user__username',)
    readonly_fields = ('display_snacks_for_week',)

    def display_snacks_for_week(self, obj):
        snacks_by_day = obj.get_snacks_for_week()
        result = ""
        for day, snacks in snacks_by_day.items():
            result += f"{day}:\n"
            for snack in snacks:
                result += f"  - {snack.name} (Seller: {snack.seller.username})\n"
        return result

    display_snacks_for_week.short_description = 'Snacks for the Week'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'seller', 'snack', 'order_date', 'get_store_name')
    search_fields = ('customer__username', 'seller__username', 'snack__name', 'seller__store_name')

    def get_store_name(self, obj):
        return obj.seller.store_name
    get_store_name.short_description = 'Store Name'

admin.site.register(User, CustomUserAdmin)
admin.site.register(Snack, SnackAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Order, OrderAdmin)