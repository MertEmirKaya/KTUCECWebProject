from django.urls import path,include
from .views import (ProfileModelListAPIView,
                    RegistrationAPIView,
                    DeleteProfileAPIView,
                    ProfileDetailAPIView,UpdateProfileModelView,ChangePasswordAPIView,LoginAPIView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',ProfileModelListAPIView.as_view()),
    path('create/',RegistrationAPIView.as_view()),
    path('<int:pk>/delete/',DeleteProfileAPIView.as_view()),
    path('<int:pk>',ProfileDetailAPIView.as_view()),
    path('<int:pk>/update/',UpdateProfileModelView.as_view()),
    path("<int:pk>/change-password/",ChangePasswordAPIView.as_view()),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #  path('logout/', LogoutView.as_view(), name='logout'),
     path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]