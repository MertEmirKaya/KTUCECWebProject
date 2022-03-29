
from rest_framework import serializers
from registration.models import ProfileModel
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProfileModel
        fields=['id','bio','username','first_name','last_name','email','phone','departmand','grade','register_date','created_time','school_number','fee','password']
        extra_kwargs = {'password1': {'write_only': True},'password2': {'write_only': True}, }

    def validate_phone(self,value):
        if len(value) !=10:
            raise serializers.ValidationError("Telefon numarası 10 haneli girilmelidir.")
        return value

    

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)


