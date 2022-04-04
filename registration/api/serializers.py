from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from registration.models import ProfileModel
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class ProfileModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ProfileModel
        fields=['id','bio','username','first_name','last_name','email','phone','departmand','grade','created_time','school_number','password']
        read_only_fields=('fee','register_date')
        write_only_fields = ('password','password1','password2',)
    def validate_phone(self,value):
        if len(value) !=10:
            raise serializers.ValidationError("Telefon numarası 10 haneli girilmelidir.")
        return value

    

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    model=ProfileModel
    old_password=serializers.CharField(required=True,write_only=True)
    password1=serializers.CharField(required=True,write_only=True)
    password2=serializers.CharField(required=True,write_only=True)
    email=serializers.EmailField(required=True,write_only=True)


    def validate(self, data):
        if data['password1']!=data['password2']:
            raise serializers.ValidationError({"Error":"Passwords must  be the same!"})


        profile=ProfileModel.objects.get(email=data['email'])
        if profile.password != data["old_password"]:
            print(profile.password)
            print(make_password(data["old_password"]))
            raise serializers.ValidationError("Password isn't true.")


        return data


    def validate_password1(self,value):
        validate_password(value)
        return value



    def update(self, instance, validated_data):

        instance.set_password(validated_data['password1'])
        instance.save()

        return instance
