from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from PIL import Image
# Create your models here.

def upload_to(instance, filename):
    return f'profile_photos/{instance.id}/{filename}'

class ProfileModel(AbstractUser):
    # id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    bio=models.TextField(null=True,blank=True)
    school_number=models.CharField(max_length=20,unique=True,null=True,blank=True)
    phone=models.CharField(max_length=20,unique=True,null=True,blank=True)
    departmand=models.CharField(max_length=50,null=True,blank=True)
    classes=[('0','Hazırlık Sınıfı'),('1','Birinci Sınıf'),('2','İkinci Sınıf'),('3','Üçüncü Sınıf'),('4','Dördüncü Sınıf'),('5','4+')]
    grade=models.CharField(max_length=20,choices=classes,null=True,blank=True)
    fee=models.BooleanField(default=False,null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    register_date=models.DateField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to=upload_to)
    role=models.CharField(max_length=90,default='member')

    def __str__(self) -> str:
        return self.username   


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            img=Image.open(self.image.path)
            if img.height>600 or img.width>600:
                output_size=(600,600)
                img.thumbnail(output_size)
                img.save(self.image.path)
        

    