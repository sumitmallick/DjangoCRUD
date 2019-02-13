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

# def product_create(request):
# 	form = ProductCreateForm()
# 	if form.is_valid():
# 		ab = form.save(commit=False)
# 		ab.save()
# 		return redirect('product_list')

# 	return render(request, 'crud/product_create.html', {'form':form})


class PromiseCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
