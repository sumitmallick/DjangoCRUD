from django.urls import path, include, reverse_lazy
from .views import product_list, PromiseCreateView
from .models import Product


urlpatterns = [
	path('', product_list , name='product_list'),
	path('create/', PromiseCreateView.as_view(model=Product ,  success_url=reverse_lazy('product_list')) , name='product_create')
]