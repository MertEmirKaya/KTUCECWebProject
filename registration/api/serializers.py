from dataclasses import fields
from rest_framework import serializers
from registration.models import ProfileModel

class ProfileModelSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=ProfileModel
        fields='__all__'




        