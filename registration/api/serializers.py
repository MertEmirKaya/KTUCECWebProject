
from rest_framework import serializers
from registration.models import ProfileModel
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileModel
        fields=['bio','username','first_name','last_name','email','phone','departmand','grade','register_date','created_time','school_number','fee',]
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
            
        }



    def create(self, validated_data):
        username=validated_data['first_name']+" "+validated_data['last_name']
        return super().create(validated_data)