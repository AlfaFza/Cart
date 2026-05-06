from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.delivery_dashboard, name='delivery_dashboard'),
    path('update/<int:order_id>/', views.update_status, name='update_status'),
]