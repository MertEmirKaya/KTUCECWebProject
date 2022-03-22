from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EventsModel(models.Model):
    name=models.CharField(max_length=100,)
    organizer=models.CharField(max_length=100,blank=True,null=True)
    events_date=models.DateTimeField()
    announcement_date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=100,blank=True)
    statement=models.TextField()
    content=models.CharField(max_length=90,blank=True)

    def __str__(self) -> str:
        return self.name
    