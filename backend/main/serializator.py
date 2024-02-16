from rest_framework import serializers
from .models import Operation, Type, Category

class OperationSerializer(serializers.ModelSerializer):
		type_r = serializers.SerializerMethodField(read_only=True)
		category_r = serializers.SerializerMethodField(read_only=True)
		class Meta:
			model = Operation
			fields = ['name', 'category','type','type_r', 'category_r',  'sum', 'already_done', 'created_till', 'created_at','id']
		def get_type_r(self,obj):
				try:
					type = Type.objects.get(id=obj.type.id)
					return str(type)
				except:
					return ""
				
		def get_category_r(self,obj):
				try:
					cat = Category.objects.get(id=obj.category.id)
					return str(cat)
				except:
					return ""
				
		

		
