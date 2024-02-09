
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import *
urlpatterns = [
      path('',Main.as_view(), name ='home'),
	  	
]