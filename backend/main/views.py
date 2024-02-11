from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Operation,Type,Category
from .serializator import OperationSerializer
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from datetime import datetime, timedelta

class MainView(APIView):
	permission_classes=[IsAuthenticated,]
	def get(self,request,*args,**kwargs):
		current_date = datetime.now().date()
		# Calculate the date 30 days ago
		thirty_days_ago = current_date - timedelta(days=30)
		try:
			#cats models
			id = kwargs.get("id",None)
			if id is not None:
				operation_obj = Operation.objects.get(id=id)
				oper_ser = OperationSerializer(operation_obj)
				return Response({"operation":oper_ser.data})
			income_cat = Category.objects.get(name='Income')
			spend_cat = Category.objects.get(name='Spend')
			saving_cat = Category.objects.get(name='Saving')
			budget_cat = Category.objects.get(name='Budget')
			goal_cat = Category.objects.get(name='Financial_Goal')

			#orm requests

			incomes = Operation.objects.filter(category=income_cat,created_by=request.user,created_at__gte=thirty_days_ago)
			spends = Operation.objects.filter(category=spend_cat,created_by=request.user,created_at__gte=thirty_days_ago)
			savings = Operation.objects.filter(category=saving_cat,created_by=request.user)
			budgets = Operation.objects.filter(category=budget_cat,created_by=request.user)
			goals = Operation.objects.filter(category=goal_cat,created_by=request.user)

			#serializers

			incomes_ser = OperationSerializer(incomes,many=True)
			spends_ser = OperationSerializer(spends,many=True)
			savings_ser = OperationSerializer(savings,many=True)
			budgets_ser = OperationSerializer(budgets,many=True)
			goals_ser = OperationSerializer(goals,many=True)
			#ser = OperationSerializer(list(incomes)+list(spends)+list(savings)+list(budgets)+list(goals),many=True) - common serialzier

			return Response({
				"incomes":incomes_ser.data,
				"spends":spends_ser.data,
				"savings":savings_ser.data,
				"budgets":budgets_ser.data,
				"goals":goals_ser.data
			})
		
		except Exception as e:
				return Response({"error": str(e)})

	
	def post(self,request):
			try:
				data = request.data
				user = request.user
				# Ensure type and category are converted to corresponding objects
				if 'type' in request.data and data['type'] !="":
					data['type'] = Type.objects.get(name=data['type']).id
				if 'category' in request.data and data['category'] !="":
					data['category'] = Category.objects.get(name=data['category']).id
				# Validate and save operation
				serializer = OperationSerializer(data=data)
				serializer.is_valid(raise_exception=True)
				serializer.save(created_by=user)
				return Response({"data": serializer.data})
			except Exception as e:
				return Response({"error": str(e)})
	def patch(self,request,*args,**kwargs):
		id = kwargs.get("id",None)
		try:
			if id is not None:
				data = request.data
				user = request.user
				instance = Operation.objects.get(id=id)
				if 'type' in request.data and data['type'] !="":
					data['type'] = Type.objects.get(name=data['type']).id
				if 'category' in request.data and data['category'] !="":
					data['category'] = Category.objects.get(name=data['category']).id
				serializer = OperationSerializer(instance,data=data)
				serializer.is_valid(raise_exception=True)
				serializer.save(created_by=user)
				return Response({"data": serializer.data})
		except Exception as e:
				return Response({"error": str(e)})

	def delete(self,request,*args,**kwargs):
		id = kwargs.get("id",None)
		if id is not None:
			try:
				instance = Operation.objects.get(id=id)
				instance.delete()
				return Response({"info":"successfully deleted"})
			except Exception as e:
				return Response({"error": str(e)})


class SearchView(generics.ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'type__name','category__name','created_at','sum'] 

		



