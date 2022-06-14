from django.urls import path
from .views import EventModelDetailAPIView, EventModelListAPIView
urlpatterns = [
    path('',EventModelListAPIView.as_view()),
    path('<int:pk>',EventModelDetailAPIView.as_view()),

]