from django.urls import path
from . import views
from shop.models import *
from .models import *

urlpatterns = [

    path('cart_details',views.cart_details,name="cart_details"),
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('cart_decrement/<int:product_id>/',views.min_cart,name="cart_decrement"),
    path('remove/<int:product_id>/',views.cart_delete,name="remove"),
    path('checkout/', views.checkout, name='checkout'),
    path('place-order/', views.place_order, name='place_order'),
    path('orders/', views.orders_view, name='orders'),
    path('submit_order/', views.submit_order, name='submit_order'),

]