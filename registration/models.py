
from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class ProfileModel(AbstractUser):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    bio=models.TextField(null=True,blank=True)
    school_number=models.CharField(max_length=20,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    departmand=models.CharField(max_length=50,null=True,blank=True)
    classes=[('Hazırlık Sınıfı','Hazırlık Sınıfı'),('Birinci Sınıf','Birinci Sınıf'),('İkinci Sınıf','İkinci Sınıf'),('Üçüncü Sınıf','Üçüncü Sınıf'),('Dördüncü Sınıf','Dördüncü Sınıf'),('4+','4+')]
    grade=models.CharField(max_length=20,choices=classes)
    fee=models.BooleanField(default=False,null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    register_date=models.DateField(null=True,blank=True)
    


    def __str__(self) -> str:
        return self.username   



