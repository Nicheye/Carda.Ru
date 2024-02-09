from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	username = models.CharField(max_length=255,unique=True)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	name = models.CharField(max_length=52,default="")
	second_name = models.CharField(max_length=52,default="")
	date_birth = models.DateField(auto_now_add=False,default="2000-08-04")
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []