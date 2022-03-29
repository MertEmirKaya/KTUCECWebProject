from django.urls import path,include
from .views import EventModelAPIView,EventModelDetailAPIView, EventModelListAPIView
urlpatterns = [
    path('',EventModelAPIView.as_view()),
    path('<str:name>',EventModelDetailAPIView.as_view()),
    path('',EventModelListAPIView.as_view())
]