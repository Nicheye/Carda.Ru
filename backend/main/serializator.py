from rest_framework import serializers
from .models import Operation, Type, Category

class OperationSerializer(serializers.ModelSerializer):
		# type = serializers.SerializerMethodField()
		# category = serializers.SerializerMethodField()
		class Meta:
			model = Operation
			fields = ['name', 'category','type', 'sum', 'already_done', 'created_till', 'created_at','id']
		# def get_type(self,obj):
				
		# 		type = Type.objects.get(id=obj.type.id)
		# 		return str(type)
				
		# def get_category(self,obj):
		
		# 		cat = Category.objects.get(id=obj.category.id)
		# 		return str(cat)
				
		

		
