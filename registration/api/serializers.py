from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from registration.models import ProfileModel
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password



class ProfileModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ProfileModel
        fields=['id','bio','username','first_name','last_name','email','phone','departmand','grade','created_time','school_number','password','image']
        read_only_fields=('fee','register_date')
        write_only_fields = ('password','password1','password2',)
    def validate_phone(self,value):
        if len(value) !=10:
            raise serializers.ValidationError("Telefon numarası 10 haneli girilmelidir.")
        return value

    

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = str(instance.first_name+instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.school_number = validated_data.get('school_number', instance.school_number)
        instance.phone= validated_data.get('phone', instance.phone)
        instance.departmand= validated_data.get('departmand', instance.departmand)
        instance.grade= validated_data.get('grade', instance.grade)
        instance.image= validated_data.get('image', instance.image)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    model=ProfileModel
    old_password=serializers.CharField(required=True,write_only=True)
    password1=serializers.CharField(required=True,write_only=True)
    password2=serializers.CharField(required=True,write_only=True)
    email=serializers.EmailField(required=True,write_only=True)


    def validate(self, data):
        if data['password1']!=data['password2']:
            raise serializers.ValidationError({"Error":"Passwords must be the same!"})

        return data


    def validate_password1(self,value):
        validate_password(value)
        return value



    def update(self, instance, validated_data):

        instance.set_password(validated_data['password1'])
        instance.save()

        return instance
