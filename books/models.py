
from django.db import models
from django.conf import settings
import uuid
# Create your models here.

def upload_to(instance, filename):
    return f'books/{instance.book}/{filename}'

class BookModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    user_who_got=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True,blank=True)
    available=models.BooleanField(default=True)
    date_of_giving=models.DateField(null=True,blank=True)
    



    def __str__(self) -> str:
        return self.title    

class ImageBookModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(null=True,blank=True,upload_to=upload_to)

    def __str__(self) -> str:
        return f'{self.book} image'