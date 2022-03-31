from rest_framework import serializers

from survey.models import SurveyModel

class SurveyModelSerializer(serializers.ModelSerializer):
    questions=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=SurveyModel
        fields='__all__'