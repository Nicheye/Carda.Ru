from datetime import date
from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'second_name', 'date_birth','age']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_age(self, obj):
        today = date.today()
        age = relativedelta(today, obj.date_birth).years
        return age

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
