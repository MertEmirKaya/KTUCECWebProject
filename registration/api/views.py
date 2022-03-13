
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from  registration.models import ProfileModel
from .serializers import ProfileModelSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
class ProfileModelAPIView(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer


class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset=ProfileModel.objects.all()
    serializer_class=ProfileModelSerializer
    
    def retrieve(self, request, *args, **kwargs):
        username=self.kwargs.get("user__username")
        profile = get_object_or_404(ProfileModel, user__username=username)
        serializer=ProfileModelSerializer(profile)
        return Response(serializer.data)



class RegistrationAPIView(generics.CreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer

    def create(self, request, *args, **kwargs):
        profile_data=request.data

        new_user=User.objects.create_user(first_name=profile_data['first_name'],
                                     last_name=profile_data['last_name'],
                                     username=str(profile_data['first_name']+profile_data['last_name']),
                                     email=profile_data['email'],
                                     password=profile_data['password'],
                                        
                                        )
        new_user.save()



        new_profile=ProfileModel.objects.create(user=new_user,
                                                bio=profile_data['bio'],
                                                school_number=profile_data['school_number'],
                                                phone=profile_data['phone'],
                                                departmand=profile_data['departmand'],
                                                grade=profile_data['grade'],
                                                fee=bool(profile_data['fee']),
                                                register_date=profile_data['register_date'],
        
        )
        new_profile.save()
        serializer=ProfileModelSerializer(new_profile)

        return Response(serializer.data)

class DeleteProfileAPIView(generics.RetrieveDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer


    def retrieve(self, request, *args, **kwargs):
        username=self.kwargs.get("user__username")
        profile = get_object_or_404(ProfileModel, user__username=username)
        serializer=ProfileModelSerializer(profile)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):

        username=self.kwargs.get("user__username")
        
        profile = get_object_or_404(ProfileModel, user__username=username)
        serializer=ProfileModelSerializer(profile)
        profile.delete()
        return Response(serializer.data)



