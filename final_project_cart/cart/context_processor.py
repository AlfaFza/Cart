from . models import *
from . views import *
# def count(request):
#     item_count=0
#     if 'admin' in request.path:
#         return {}
#     else:
#         try:
#             ct=cartlist.objects.filter(cart_id=c_id(request))
#             cti=items.objects.all().filter(cart=ct[:1])
#             for c in cti:
#                 item_count +=c.quan
#         except cartlist.DoesNotExist:
#             item_count=0
#         return dict(itc=item_count)

def count(request):
    item_count = 0
    order_count = 0
    if 'admin' in request.path:
        return {}
    try:
        if request.user.is_authenticated:
            cart = cartlist.objects.filter(cart_id=c_id(request))
            items_in_cart = items.objects.filter(cart=cart[:1])
            item_count = sum(item.quan for item in items_in_cart)

            # Count orders for the user
            order_count = Order.objects.filter(user=request.user).count()
    except cartlist.DoesNotExist:
        pass

    return {'itc': item_count, 'order_count': order_count}
