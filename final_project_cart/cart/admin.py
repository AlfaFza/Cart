from django.contrib import admin

# Register your models here.
from .models import *



#admin can handle  order 


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'total_amount', 'date')
    list_filter = ('status', 'date')
    search_fields = ('order_id', 'user__username', 'user__email')
    inlines = [OrderItemInline]

    # Add a dropdown to change the status directly from the list view
    list_editable = ('status',)

    # Allow editable fields in the admin detail view
    fieldsets = (
        (None, {
            'fields': ('order_id', 'user', 'address', 'total_amount', 'status', 'date')
        }),
    )

    readonly_fields = ('order_id', 'user', 'total_amount', 'date')

    # Define permissions for updating the status
    def has_change_permission(self, request, obj=None):
        return True
    
