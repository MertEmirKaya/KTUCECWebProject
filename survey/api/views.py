from rest_framework import generics
from survey.api.serializers import SurveyModelSerializer

from survey.models import SurveyModel

class SurveyModelListAPI(generics.ListAPIView):
    queryset=SurveyModel.objects.all()
    serializer_class=SurveyModelSerializer
    