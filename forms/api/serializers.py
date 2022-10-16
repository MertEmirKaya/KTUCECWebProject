from pyexpat import model
from rest_framework import serializers
from forms.models import Survey,Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'


class SurverSerializer(serializers.ModelSerializer):
    questions=serializers.StringRelatedField(many=True)
    class Meta:
        model=Survey
        fields='__all__'
