from django.urls import path
from .views import SurveyListAPIView
urlpatterns = [
    path('',SurveyListAPIView.as_view())

]