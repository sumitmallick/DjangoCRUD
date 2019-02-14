from django.contrib.auth import views
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/', views.login_user, name='login_user'),

    path('logout/', views.logout_user, name='logout_user'),

    path('', include('django.contrib.auth.urls')),

    path('change-password/', views.change_password, name='change_password'),
]