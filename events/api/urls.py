from django.urls import path,include
from .views import EventModelDetailAPIView, EventModelListAPIView
urlpatterns = [
    path('',EventModelListAPIView.as_view()),
    path('<str:name>',EventModelDetailAPIView.as_view()),

]