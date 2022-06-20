from rest_framework import status
from rest_framework import generics
from  registration.models import ProfileModel
from .serializers import ProfileModelSerializer,ChangePasswordSerializer
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework import serializers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

class LoginAPIView(TokenObtainPairView):
    '''
    
    '''
    def post(self, request, *args, **kwargs):
        email=request.data['email']
        request.POST._mutable = True
        profile=ProfileModel.objects.get(email=email)
        request.data['username']=profile.username
        request.POST._mutable = False
        return super().post(request, *args, **kwargs)


class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class ProfileModelListAPIView(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username','first_name','last_name','bio']

    


class ProfileDetailAPIView(generics.GenericAPIView):
    '''
    JWT token is required!
    An Api which returns the requested user's profile
    '''

    serializer_class=ProfileModelSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        key='super-secret'
        payload={"id":str(request.user.id),}
        token= jwt.encode(payload, key)
        
        decoded = jwt.decode(token, options={"verify_signature": False})
        
        profile=ProfileModel.objects.get(id=decoded['id'])
        profile_serializer=ProfileModelSerializer(profile)
        return Response(data=profile_serializer.data,status=status.HTTP_200_OK)


class RegistrationAPIView(generics.CreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["username"]=str(request.data['first_name']+request.data['last_name'])
        if request.data['password1']!=request.data['password2']:
            raise serializers.ValidationError('passwords must be the same!')
        request.data['password']=request.data['password1']
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)
        


class DeleteProfileAPIView(generics.DestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
    

class UpdateProfileModelView(generics.UpdateAPIView):
    serializer_class=ProfileModelSerializer
    queryset=ProfileModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class=ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    queryset=ProfileModel.objects.all()
             
    def get_object(self):
        return self.request.user
            
     