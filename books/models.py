from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookModel(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    user_who_got=models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    date_of_giving=models.DateField()
    available=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title    