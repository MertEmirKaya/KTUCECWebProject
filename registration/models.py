from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from PIL import Image
import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings
# Create your models here.
username_validator = UnicodeUsernameValidator()
def upload_to(instance, filename):
    return f'profile_photos/{instance.id}/{filename}'



class ProfileModel(AbstractUser):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    email = models.EmailField(("email address"), blank=True,unique=True)
    username = models.CharField(("username"),default=uuid.uuid4,max_length=150,unique=True,help_text=("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),validators=[username_validator], error_messages={"unique": ("A user with that username already exists."),})
    bio=models.TextField(null=True,blank=True)
    school_number=models.CharField(max_length=20,unique=True,null=True,blank=True)
    phone=models.CharField(max_length=10,unique=True,null=True,blank=True)
    department=models.CharField(max_length=50,null=True,blank=True)
    classes=[('0','Hazırlık Sınıfı'),('1','Birinci Sınıf'),('2','İkinci Sınıf'),('3','Üçüncü Sınıf'),('4','Dördüncü Sınıf'),('4+','5')]
    grade=models.CharField(max_length=20,choices=classes,null=True,blank=True)
    fee=models.BooleanField(default=False,null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    register_date=models.DateField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to=upload_to)
    role=models.CharField(max_length=90,default='member',null=True,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

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
        

   

    def random_username(sender, instance, **kwargs):
        if not instance.username:
            instance.username = uuid.uuid4().hex[:30]

