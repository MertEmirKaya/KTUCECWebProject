from django.urls import path,include
from .views import BookModelListAPIView,BookModelDetailAPIView
urlpatterns = [
    path('',BookModelListAPIView.as_view()),
    path('<str:title>',BookModelDetailAPIView.as_view())
]