from django.shortcuts import render

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'contact/contact_list.html')
            else:
                return render(request, 'contact/templates/contact/contact_list.html', {'error_message': 'Invalid Login'})
        else:
            render(request, 'user/login.html',{'error_message': 'Invalid Login'})
    return render(request, 'user/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'user/login.html', context)


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
                login(user, request)
                return render(request, 'contact/contact_list.html')
    context = {
        "form": form,
    }
    return render(request, 'user/login.html')

