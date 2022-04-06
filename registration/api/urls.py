from django.urls import path,include
from .views import ProfileModelListAPIView,RegistrationAPIView,DeleteProfileAPIView,ProfileDetailAPIView,UpdateProfileModelView,ChangePasswordAPIView


urlpatterns = [
    path('',ProfileModelListAPIView.as_view()),
    path('create/',RegistrationAPIView.as_view()),
    path('<str:username>/delete/',DeleteProfileAPIView.as_view()),
    path('<str:username>',ProfileDetailAPIView.as_view()),
    path('<str:username>/update/',UpdateProfileModelView.as_view()),
    path("<str:username>/change-password/",ChangePasswordAPIView.as_view()),
]