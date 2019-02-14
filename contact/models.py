from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	contactno = models.IntegerField()
