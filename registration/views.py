from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .forms import UserForm
from contact.views import Contact

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'registration/mlogin.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Contact.objects.all()
                return redirect('contact_list')
            else:
                return render(request, 'registration/mlogin.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/mlogin.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/mlogin.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Contact.objects.all()
                return redirect('contact_list')
    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('register:login_user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'register/change_password.html', {
        'form': form
    })

