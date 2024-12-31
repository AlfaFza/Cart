from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import *


# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect("register")
        return redirect("/")
    else:
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid request")
            return redirect("login")

    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("/")


class profile(View):
    def get(self,request):
        form = CustomerProfileForm()
        totalitem =0 
        wishlist=0
        # if request.user.is_authenticated:
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        #     c=Cart.objects.filter(user=request.user)
        #     for p in c:
        #         totalitem= totalitem + p.quantity
    
        return render(request,'profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            print(user)
            name= form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state =form.cleaned_data['state']
            
            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations! Profile Save Successfully')
        else:
            messages.warning(request,'Invalid Input Data')
        return render(request,'profile.html',locals())
    
    
def address(request):
    totalitem =0 
    # wishlist=0
    # if request.user.is_authenticated:
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    #     c=Cart.objects.filter(user=request.user)
    #     for p in c:
    #         totalitem= totalitem + p.quantity
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk) 
        # see what is appear in form field 'instance = add'
        form = CustomerProfileForm(instance=add) 
        return render(request,'updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name= form.cleaned_data['name']
            add.locality = form.cleaned_data[' locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.state =form.cleaned_data['state']
            add.save()
            messages.success(request,'Congratulations! Profile Save Successfully')
        else:
            messages.warning(request,'Invalid Input Data')
     
        return redirect('address')