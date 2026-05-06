from django.db import models

# Create your models here.
from accounts.models import Customer
from shop.models import products
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from delivery.models import DeliveryBoy
from django.utils import timezone

User = get_user_model()

#cart section

class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.cart_id
class items(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return  self.prodt
    def total(self):
        return self.prodt.price*self.quan

#order section
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Preparing', 'Preparing'),
        ('Assigned', 'Assigned'),
        ('Collected', 'Collected'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Failed', 'Failed'),  # delivery failed
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    address =models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date = models.DateTimeField(auto_now_add=True)
    PAYMENT_METHOD_CHOICES = [
            ('COD', 'Cash on Delivery'),
            ('ONLINE', 'Online Payment'),
        ]

    PAYMENT_STATUS_CHOICES = [
            ('Pending', 'Pending'),
            ('Paid', 'Paid'),
            ('Failed', 'Failed'),
        ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='COD')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    
    delivery_boy = models.ForeignKey(
            DeliveryBoy,
            on_delete=models.SET_NULL,
            null=True,
            blank=True
        )
    

    picked_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    cash_received = models.BooleanField(default=False)
    
    def get_total(self):
        return sum(item.total() for item in self.items.all())
    
    def save(self, *args, **kwargs):

        if self.status == 'Delivered' and self.payment_method == 'COD':
            self.payment_status = 'Paid'
            self.cash_received = True

        if self.status == 'Cancelled':
            if self.payment_method == 'ONLINE':
                self.payment_status = 'Failed'
                
        if self.delivery_boy and self.status == 'Confirmed':
            self.status = 'Assigned'
            self.assigned_at = timezone.now()
            
        # when delivery boy is assigned first time
        if self.delivery_boy and not self.assigned_at:
            self.assigned_at = timezone.now()
            self.status = 'Assigned'

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Order {self.order_id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product.name} - {self.order.order_id}"

