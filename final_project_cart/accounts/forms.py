from django import forms

from django.contrib.auth.models import User
from .models import Customer
from .views import *
from django.core.validators import MaxLengthValidator

# from accounts.views import validate_mobile_length


class CustomerProfileForm(forms.ModelForm):
    zipcode = forms.CharField(max_length=6, validators=[MaxLengthValidator(6)])
    
    class Meta:
       model =Customer
       fields =['name','locality','city','mobile','state','zipcode']
       widgets={
           'name': forms.TextInput(attrs={'class':'form-control'}),
           'locality': forms.TextInput(attrs={'class':'form-control'}),
           'city': forms.TextInput(attrs={'class':'form-control'}),
           'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 9852 8855 252', 'value': '+91 9852 8855 252'}),
           'state': forms.Select(attrs={'class':'form-control'}),
           'zipcode': forms.NumberInput(attrs={'class':'form-control'}),
       }
    
    # def clean_mobile(self):
    #     mobile = self.cleaned_data.get('mobile')
    #     validate_mobile_length(mobile)
    #     return mobile