from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoy
from cart.models import *

@login_required
def delivery_dashboard(request):
    try:
        delivery_boy = DeliveryBoy.objects.get(user=request.user)
    except DeliveryBoy.DoesNotExist:
        return render(request, 'delivery/no_access.html')

    orders = Order.objects.filter(delivery_boy=delivery_boy)

    return render(request, 'delivery/dashboard.html', {'orders': orders})


@login_required
def update_status(request, order_id):
    order = Order.objects.get(id=order_id)
    delivery_boy = DeliveryBoy.objects.get(user=request.user)

    if order.delivery_boy != delivery_boy:
        return redirect('delivery_dashboard')

    status = request.POST.get('status')
  # ✔ Picked
    # if status == 'picked' and order.status == 'Assigned':
    #     order.status = 'Collected'
    if status == 'picked':
        order.status = 'Out for Delivery'
        order.picked_at = timezone.now()
        
    # ✔ Delivered
    elif status == 'delivered' and order.status in ['Collected', 'Out for Delivery']:
        order.status = 'Delivered'
        order.delivered_at = timezone.now()

    # ✔ Cash received (COD only)
    elif status == 'cash' and order.status == 'Delivered' and order.payment_method == 'COD':
        order.payment_status = 'Paid'
        order.cash_received = True

    order.save()

    return redirect('delivery_dashboard')