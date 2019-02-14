from django.urls import path, reverse_lazy
from . import views
from .models import Contact


urlpatterns = [
    path('contacts', views.ContactList.as_view(), name='contact_list'),
    path('detail/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    path('create', views.ContactCreate.as_view(model=Contact, success_url=reverse_lazy('contact_list')), name='contact_create'),
    path('update/<int:pk>', views.ContactUpdate.as_view(model=Contact, success_url=reverse_lazy('contact_list')), name='contact_update'),
    path('delete/<int:pk>', views.ContactDelete.as_view(model=Contact, success_url=reverse_lazy('contact_list')), name='contact_delete'),
]
