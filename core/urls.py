from django.urls import path
from . import views



urlpatterns = [
	path('employees/', views.emp_list, name="emp_list"),
	path('employees/create/', views.emp_create, name="emp_create"),
	path('employees/delete/<int:id>', views.emp_delete, name="empdelete"),
	path('employees/view/<int:id>', views.emp_detail, name="emp_detail"),
	path('employees/update/<int:id>', views.emp_update, name="emp_update"),

]