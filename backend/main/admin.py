from django.contrib import admin

# Register your models here.
from .models import Type,Category,Operation
admin.site.register(Operation)
admin.site.register(Category)
admin.site.register(Type)