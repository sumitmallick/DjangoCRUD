from django.urls import path
from . import views
from .views import login_user, logout_user, register


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]