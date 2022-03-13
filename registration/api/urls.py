from django.urls import path,include
from .views import ProfileModelAPIView,RegistrationAPIView,DeleteProfileAPIView,ProfileDetailAPIView
urlpatterns = [
    path('profiles/',ProfileModelAPIView.as_view()),
    path('create/',RegistrationAPIView.as_view()),
    path('profiles/<str:user__username>/delete/',DeleteProfileAPIView.as_view()),
    path('profiles/<str:user__username>',ProfileDetailAPIView.as_view()),    

    
]