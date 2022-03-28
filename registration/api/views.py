
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from  registration.models import ProfileModel
from .serializers import ProfileModelSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework import serializers


class ProfileModelListAPIView(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username','first_name','last_name','bio']

    


class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset=ProfileModel.objects.all()
    serializer_class=ProfileModelSerializer
    lookup_field='username'
    permission_classes = [IsAuthenticated]
    





class RegistrationAPIView(generics.CreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    lookup_field='username'
    def create(self, request, *args, **kwargs):
        username=str(request.data['first_name']+" "+request.data['last_name'])
        return super().create(request, *args, **kwargs)
        


class DeleteProfileAPIView(generics.RetrieveDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        username=self.kwargs.get("username")
        profile = get_object_or_404(ProfileModel,username=username)
        serializer=ProfileModelSerializer(profile)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        raw_request_token=request.META.get('HTTP_AUTHORIZATION')
        username=self.kwargs.get("username")
        profile = get_object_or_404(ProfileModel,username=username)

        if raw_request_token:
            request_token=raw_request_token[6:]
            user_token=Token.objects.get(user=profile)

            if str(request_token)==str(user_token):
                serializer=ProfileModelSerializer(profile)
                profile.delete()
                return Response(status=status.HTTP_401_UNAUTHORIZED)






class UpdateProfileModelView(generics.RetrieveUpdateAPIView):
    serializer_class=ProfileModelSerializer
    queryset=ProfileModel.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        username=self.kwargs.get("username")
        profile = get_object_or_404(ProfileModel,username=username)
        serializer=ProfileModelSerializer(profile)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        raw_request_token=request.META.get('HTTP_AUTHORIZATION')
        username=self.kwargs.get("username")
        profile=ProfileModel.objects.get(username=username)
    
        if raw_request_token:
            request_token=raw_request_token[6:]
            user_token=Token.objects.get(user=profile)
            if str(request_token)==str(user_token):
                
                updated_data=request.data      
                updated_profile=ProfileModel.objects.filter(username=username).update(
                                                            first_name=updated_data['first_name'],
                                                            last_name=updated_data['last_name'],
                                                            email=updated_data['email'],
                                                            bio=updated_data['bio'],
                                                            school_number=str(updated_data['school_number']),
                                                            phone=updated_data['phone'],
                                                            departmand=updated_data['departmand'],
                                                            grade=updated_data['grade'],
                                                            fee=bool(updated_data['fee']),
                                                            register_date=updated_data['register_date'],
                
                )
                return Response(status=status.HTTP_200_OK)     
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
             

          