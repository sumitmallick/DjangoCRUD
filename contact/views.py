from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Contact

from .forms import ContactCreateForm
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class ContactLoginView(LoginView):
    template_name = "contact/login.html"
    redirect_authenticated_user = True

class ContactList(ListView):
	model = Contact

class ContactDetail(DetailView):
	model = Contact

class ContactCreate(SuccessMessageMixin, CreateView):
	model = Contact
	form_class = ContactCreateForm
	success_message = 'Form has been successfully submitted!'

class ContactDelete(DeleteView):
	model = Contact
	# fields = '__all__'

class ContactUpdate(UpdateView):
	model = Contact
	form_class = ContactCreateForm

def profile_page(request, pk):
    user = Contact.objects.get(id = pk)
    return render(request, 'contact/user_profile.html', {'user_profile': user})