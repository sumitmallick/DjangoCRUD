from django.urls import path, include, reverse_lazy
from .views import product_list, product_detail, PromiseCreateView, product_update, product_delete
from .models import Product


urlpatterns = [
	path('product-list', product_list , name='product_list'),
	path('product-create/', PromiseCreateView.as_view(model=Product ,  success_url=reverse_lazy('product_list')) , name='product_create'),
	path('product-delete/<int:id>', product_delete, name='product_delete'),
	path('product-update/<int:id>', product_update, name='product_update'),
	path('product-detail/<int:id>', product_detail, name='product_detail')
]