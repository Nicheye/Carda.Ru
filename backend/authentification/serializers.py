from rest_framework import serializers
from .models import User
from dateutil.relativedelta import relativedelta
from datetime import date
class UserSerializer(serializers.ModelSerializer):
	age = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields =['id','username','password','name','second_name','age']
		extra_kwargs = {
			'password':{'write_only':True}
		}
	def get_age(self,obj):
		b=date.today()
		
		return str(relativedelta(b,obj.date_birth).years)
	def create(self,validated_data):
		password = validated_data.pop('password',None)
		instance =  self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance