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

			incomes = Operation.objects.filter(category=income_cat,created_by=request.user,created_at__gte=thirty_days_ago).order_by('-created_at')
			spends = Operation.objects.filter(category=spend_cat,created_by=request.user,created_at__gte=thirty_days_ago).order_by('-created_at')
			sum_spend = 0
			for spend in spends:
				sum_spend+=spend.sum
			savings = Operation.objects.filter(category=saving_cat,created_by=request.user).order_by('-created_at')
			budgets = Operation.objects.filter(category=budget_cat,created_by=request.user).order_by('-created_at')
			budgets_completion = []
			for budget in budgets:
				dict_for_cat = {}
				spends_for_cat = Operation.objects.filter(created_by=request.user,type=budget.type,created_at__gte=thirty_days_ago,category=spend_cat)
				sum=0
				for spend in spends_for_cat:
					sum+=spend.sum
				dict_for_cat['name'] = str(budget.type)
				try:
					dict_for_cat['percentage'] = f"{ round(sum/budget.sum*100)  } % ({spend.sum}) "
				except:
					pass
				budgets_completion.append(dict_for_cat)
			goals = Operation.objects.filter(category=goal_cat,created_by=request.user).order_by('-created_at')

			#serializers

			incomes_ser = OperationSerializer(incomes,many=True)
			spends_ser = OperationSerializer(spends,many=True)
			savings_ser = OperationSerializer(savings,many=True)
			budgets_ser = OperationSerializer(budgets,many=True)
			goals_ser = OperationSerializer(goals,many=True)
			#ser = OperationSerializer(list(incomes)+list(spends)+list(savings)+list(budgets)+list(goals),many=True) - common serialzier

			return Response({
				"incomes":incomes_ser.data,
				"incomes_total":sum_spend,
				"spends":spends_ser.data,
				"savings":savings_ser.data,
				"budgets":budgets_ser.data,
				"budgets_completion":budgets_completion,
				"goals":goals_ser.data,
				
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
		permission_classes=  [IsAuthenticated,]
		serializer_class = OperationSerializer
		filter_backends = [filters.SearchFilter,filters.OrderingFilter]
		ordering_fields = ['name', 'type__name','category__name','created_at','sum'] 
		search_fields = ['name', 'type__name','category__name','created_at','sum']
		def get_queryset(self,*args,**kwargs):
			queryset = Operation.objects.filter	(created_by=self.request.user)
			return queryset 
   
	
	

		

class AiBot(APIView):
	permission_classes = [IsAuthenticated,]
	def get(self,request):
		
		current_date = datetime.now().date()
		# Calculate the date 30 days ago
		thirty_days_ago = current_date - timedelta(days=30)
		try:
			#cats models
			income_cat = Category.objects.get(name='Income')
			spend_cat = Category.objects.get(name='Spend')
			saving_cat = Category.objects.get(name='Saving')
			budget_cat = Category.objects.get(name='Budget')
			goal_cat = Category.objects.get(name='Financial_Goal')

			#orm requests

			incomes = Operation.objects.filter(category=income_cat,created_by=request.user,created_at__gte=thirty_days_ago).order_by('-created_at')
			sum_income = 0
			for income in incomes:
				sum_income+=income.sum
			
			spends = Operation.objects.filter(category=spend_cat,created_by=request.user,created_at__gte=thirty_days_ago).order_by('-created_at')
			sum_spend = ''
			for spend in spends:
				sum_spend+=f'затрата  {str(spend.type)} на {str(spend.sum)} руб'
				
				

			savings = Operation.objects.filter(category=saving_cat,created_by=request.user).order_by('-created_at')
			savings_sum=0
			for saving in savings:
				savings_sum+=saving.sum
			

			budgets = Operation.objects.filter(category=budget_cat,created_by=request.user).order_by('-created_at')
			budget_msg = ''
			for budget in budgets:
				budget_msg+=f'у меня есть бюджет {budget.sum} на {budget.type} '
			
			goals = Operation.objects.filter(category=goal_cat,created_by=request.user).order_by('-created_at')
			goal_msg = f'у меня есть цель - {goals[0].name} на сумму {goals[0].sum}'

			final_msg = f'мой доход - {sum_income} , мои расходы - {sum_spend}, мои сбережения на сумму {savings_sum} , {budget_msg} , {goal_msg} дай ответ как мне достичь моей цели,     '

			msg=ai_message(final_msg)

			return Response({"message":str(msg[155:])})

			
		
		except Exception as e:
				return Response({"error": str(e)})


import requests
import json
import warnings

def ai_message(data):
	warnings.filterwarnings('ignore', message='Unverified HTTPS request')
# Set the URL and payload for OAuth token request
	oauth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
	oauth_payload = {'scope': 'GIGACHAT_API_PERS'}
	oauth_headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept': 'application/json',
		'RqUID': 'eb1c7911-998f-4720-91d8-e5177c943f5d',
		'Authorization': 'Basic ZWIxYzc5MTEtOTk4Zi00NzIwLTkxZDgtZTUxNzdjOTQzZjVkOmZjMzhlOGVjLWZmNDYtNGZjZC1iN2E5LTdhYmU5Y2RiNDA4YQ=='
	}

	# Make OAuth token request
	oauth_response = requests.post(oauth_url, headers=oauth_headers, data=oauth_payload,verify=False)

	# Extract access token
	access_token = oauth_response.json()['access_token']

	# Set the URL and payload for chat completion request
	chat_completion_url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
	chat_completion_payload = {
		"model": "GigaChat:latest",
		"messages": [{"role": "user", "content": f"{data} ответ до 70 слов"}],
		"temperature": 1,
		"top_p": 0.1,
		"n": 1,
		"stream": False,
		"max_tokens": 512,
		"repetition_penalty": 1
	}
	chat_completion_headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Authorization': f'Bearer {access_token}'
	}

	# Make chat completion request
	chat_completion_response = requests.post(chat_completion_url, headers=chat_completion_headers, data=json.dumps(chat_completion_payload), verify=False)

	# Print the response
	message_from_ai =chat_completion_response.json()['choices'][0]['message']['content']
	return message_from_ai