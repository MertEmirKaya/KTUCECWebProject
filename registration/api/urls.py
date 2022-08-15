from django.urls import path,include
from .views import (
                    RegistrationAPIView,
                    
                    ProfileDetailAPIView,ChangePasswordAPIView,LoginAPIView,LogoutView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/',RegistrationAPIView.as_view()),
    # path('profile/delete/',DeleteProfileAPIView.as_view()),
    path('profile/',ProfileDetailAPIView.as_view()),
    # path('profile/update/',UpdateProfileModelView.as_view()),
    path("profile/change-password/",ChangePasswordAPIView.as_view()),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]