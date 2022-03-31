from django.urls import path,include
from .views import SurveyModelListAPI
urlpatterns = [
    path('',SurveyModelListAPI.as_view())    
]