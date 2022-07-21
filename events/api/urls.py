from django.urls import path
from .views import EventModelDetailAPIView, EventModelListAPIView
urlpatterns = [
    path('',EventModelListAPIView.as_view()),
    path('<uuid:pk>',EventModelDetailAPIView.as_view()),

]