from django.db import models

# Create your models here.

class SignUp(models.Model):
	name=models.CharField(max_length=20)
	mobile=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	pass1=models.CharField(max_length=20)

class studentreg(models.Model):
	firstname=models.CharField(max_length=20)
	lastname=models.CharField(max_length=20)
	birthdate=models.CharField(max_length=20)
	gender=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	mobile=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	
class AdminNotice(models.Model):
	ndate1=models.CharField(max_length=20)
	subject=models.CharField(max_length=50)