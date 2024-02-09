from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentification.serializers import UserSerializer
# Create your views here.

class Main(APIView):
	permission_classes = [IsAuthenticated,]
	def get(self,request):
		user = request.user
		user_ser = UserSerializer(user)
		return Response({"user":user_ser.data})
