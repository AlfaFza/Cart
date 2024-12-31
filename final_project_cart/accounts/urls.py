from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [

    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
      #    Password reset link sent by email.
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='password_reset_complete'),
    
    path("changepassword/", auth_views.PasswordChangeView.as_view(template_name='changepassword.html'),name='passwordchange'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
   
    # 
    path('profile', views.profile.as_view(), name="profile"),
    path('address',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
]
