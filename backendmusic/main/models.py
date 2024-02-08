from django.db import models
from authentification.models import User
# Create your models here.
class Type(models.Model):
	name = models.CharField(max_length=20)

class Income(models.Model):
	type = models.ForeignKey(Type,on_delete=models.CASCADE)
	sum = models.PositiveIntegerField()
	created_by = models.ForeignKey(User,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)

class Spend(models.Model):
	type = models.ForeignKey(Type,on_delete=models.CASCADE)
	sum = models.PositiveIntegerField()
	created_by = models.ForeignKey(User,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)

class Saving(models.Model):
	type = models.ForeignKey(Type,on_delete=models.CASCADE)
	sum = models.PositiveIntegerField()
	created_by = models.ForeignKey(User,on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)

class Financial_Goal(models.Model):
	name = models.CharField(max_length=100)
	sum = models.PositiveIntegerField()
	created_till = models.DateField(auto_now_add=False)


class Budget(models.Model):
	
	category = models.ForeignKey(Type,on_delete=models.CASCADE)
	sum = models.PositiveIntegerField()
