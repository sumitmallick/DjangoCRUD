from .models import *
from django import forms
from django.forms import ModelForm




class ContactCreateForm(ModelForm):

	class Meta:
		model = Contact
		fields = ('name', 'email', 'address', 'contactno')


	def clean(self):
		cleaned_data = super(ContactCreateForm, self).clean()
		contactno = cleaned_data.get('contactno')
		if len(str(contactno))!=10:
			self.add_error(None, forms.ValidationError('contact no should have 10 digits'))
		return cleaned_data