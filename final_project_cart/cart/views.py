from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
# from .forms import CheckoutForm
from django.utils.crypto import get_random_string

# Create your views here.
from shop.models import products
from .models import *

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from django.shortcuts import render, redirect

# from .utils import send_order_confirmation_email 


#cart sections

@login_required(login_url='login')
def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot+=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass

    return render(request,"cart.html",{'ci':ct_items,'t':tot,'cn':count})

@login_required(login_url='login')
def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quan<c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()
    return  redirect('cart_details')


def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quan > 1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect("cart_details")

def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products,id=product_id)
    c_items = items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect("cart_details")



#checkout section

@login_required(login_url='login')
def checkout(request):
    user = request.user
    address = Customer.objects.filter(user=user)
    cart = cartlist.objects.get(cart_id=c_id(request))
    cart_items = items.objects.filter(cart=cart)
    total = sum(item.total() for item in cart_items)

    return render(request, 'checkout.html', {'address': address, 'cart_items': cart_items, 'total': total})


@login_required(login_url='login')
def place_order(request):
    if request.method == 'POST':
        user = request.user
        address_id = request.POST.get('address')
        address = Customer.objects.get(id=address_id)
        cart = cartlist.objects.get(cart_id=c_id(request))
        cart_items = items.objects.filter(cart=cart)

        # Create a unique order ID
        order_id = get_random_string(10).upper()
        total_amount = sum(item.total() for item in cart_items)

        # Create the order
        order = Order.objects.create(
            user=user, order_id=order_id, total_amount=total_amount, address=address
        )

        # Add items to the order
        for item in cart_items:
            OrderItem.objects.create(
                order=order, product=item.prodt, quantity=item.quan, price=item.prodt.price
            )
            # Decrease stock for the product
            item.prodt.stock -= item.quan
            item.prodt.save()

        # Clear the cart
        cart_items.delete()

        return redirect('submit_order')

    return redirect('checkout')

#order section


@login_required(login_url='login')
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})



@login_required(login_url='login')
def submit_order(request):
    return render(request,'submitorder.html')



# def send_order_confirmation_email(user_email, order_details):
    subject = "Order Confirmation"
    message = render_to_string('order_confirmation_email.html', {'order_details': order_details})
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)


 # Import the email function

# def place_order(request):
#     if request.method == "POST":
#         # Get the cart and order details
#         cart_items = cartlist.objects.filter(user=request.user)
#         total = sum(item.quantity * item.product.price for item in cart_items)
        
#         # Create an order
#         order = Order.objects.create(user=request.user, total=total)
#         order_details = {
#             'items': [{'name': item.product.name, 'quantity': item.quantity, 'price': item.product.price} for item in cart_items],
#             'total': total
#         }
        
#         # Send order confirmation email
#         send_order_confirmation_email(request.user.email, order_details)
        
#         # Clear the cart after placing order
#         cart_items.delete()
        
#         # Redirect to order confirmation page
#         return render(request, 'order_submitted.html', {'order': order})
#     return redirect('cart')

