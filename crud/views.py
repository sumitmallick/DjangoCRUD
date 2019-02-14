from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Product
from .forms import ProductCreateForm


def product_list(request):
	qs = Product.objects.all()
	context={
		'qs':qs
	}
	return render(request, 'crud/product_list.html', context)


class PromiseCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm

def product_delete(request, id):
	a = Product.objects.get(id=id)
	a.delete()
	return redirect('product_list')

def product_detail(request, id):
	a = Product.objects.get(id=id)
	return render(request, 'crud/product_detail.html', {'a':a})

def product_update(request, id):
	a = Product.objects.get(id=id)
	if request.method == 'POST':
		form = ProductCreateForm(request.POST, instance=a)
		if form.is_valid():
			ans = form.save(commit=False)
			ans.save()
			return redirect('product_list')

	else:
		form = ProductCreateForm(instance=a)

	return render(request, 'crud/product_form.html', {'form':form})