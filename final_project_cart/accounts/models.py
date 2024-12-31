from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Cust(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    

STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)


class Customer(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    