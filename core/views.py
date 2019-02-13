from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm



def emp_list(request):
	qs = Employee.objects.all()
	return render(request,'core/show.html', {"qs": qs})



def emp_create(request):
	form = EmployeeForm(request.POST)
	if form.is_valid():
		abc = form.save(commit=False)
		abc.save()
		return redirect('emp_list')
	return render(request, 'core/emp_create.html', {'form': form})

def emp_delete(request, id):
	a = get_object_or_404(Employee ,id=id)
	a.delete()
	return redirect('emp_list')


def emp_detail(request, id):
	a = Employee.objects.get(id=id)
	return render(request, 'core/emp_detail.html', {'a': a})



def emp_update(request, id):
	a = Employee.objects.get(id=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance=a)
		if form.is_valid():
			abc = form.save(commit=False)
			abc.save()
			return redirect('emp_list')
	else:
		form = EmployeeForm(instance=a)
	return render(request, 'core/emp_create.html', {'form': form})