from django.urls import path
from .views import EventModelDetailAPIView, UpComingEventModelListAPIView,PastEventModelListAPIView
urlpatterns = [
    path('upcoming',UpComingEventModelListAPIView.as_view()),
    path('past',PastEventModelListAPIView.as_view()),
    path('<uuid:pk>',EventModelDetailAPIView.as_view()),

]