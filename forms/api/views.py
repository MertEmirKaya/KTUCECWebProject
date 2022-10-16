from forms.models import Survey,Question
from .serializers import SurverSerializer
from rest_framework import generics


class SurveyListAPIView(generics.ListAPIView):
    queryset=Survey.objects.all()
    serializer_class=SurverSerializer    

