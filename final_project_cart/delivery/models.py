from django.db import models
from django.contrib.auth.models import User
from cart.models import *   # adjust if your app name is different

class DeliveryBoy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username