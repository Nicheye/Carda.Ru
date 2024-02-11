from django.db import models
from authentification.models import User
class Type(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self) -> str:
		return str(self.name)
	

class Category(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self) -> str:
		return str(self.name)
	

class Operation(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	category =models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
	type = models.ForeignKey(Type,on_delete=models.CASCADE,null=True,blank=True)
	sum = models.PositiveIntegerField(null=True,blank=True)
	already_done = models.PositiveIntegerField(null=True,blank=True)	
	created_till = models.DateField(auto_now_add=False,null=True,blank=True)
	created_at = models.DateField(auto_now_add=True)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self) -> str:
		return str(self.name) + " | " + str(self.category)  + " | " + str(self.sum)