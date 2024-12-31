from django.db import models

# Create your models here.
from accounts.models import Customer
from shop.models import products
from django.contrib.auth import get_user_model
from django.utils.timezone import now

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
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    address =models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - {self.order.order_id}"
