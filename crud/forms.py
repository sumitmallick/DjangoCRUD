from .models import *
from django import forms
from django.forms import ModelForm



class DateInput(forms.DateInput):
    input_type = 'date'




class ProductCreateForm(ModelForm):

	class Meta:
		model = Product
		fields = ('name', 'category', 'price', 'date_created', 'stock')

		widgets = {
            'date_created':DateInput(),
        }

