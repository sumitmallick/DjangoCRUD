from django.contrib.auth import views
from django.urls import path, include, re_path, reverse_lazy

from . import views
from django.contrib.auth import views as auth_views

from django.views.generic import RedirectView

app_name = 'userregister'

urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/', views.login_user, name='login_user'),

    path('logout/', views.logout_user, name='logout_user'),

]