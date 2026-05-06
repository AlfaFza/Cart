from django.contrib import admin
from .models import DeliveryBoy
from cart.models import Order

admin.site.register(DeliveryBoy)


# Enhance Order admin (IMPORTANT)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'status', 'payment_status', 'delivery_boy']
    list_filter = ['status', 'payment_status']
    search_fields = ['order_id', 'user__username']

admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)