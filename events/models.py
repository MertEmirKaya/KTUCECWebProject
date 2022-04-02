from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime,timedelta
# Create your models here.

class EventModel(models.Model):
    id = models.UUIDField(
         primary_key = True,default = uuid.uuid4,editable = False
         )
    name=models.CharField(max_length=100,)
    organizer=models.CharField(max_length=100,blank=True,null=True)
    events_date=models.DateTimeField()
    announcement_date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=100,blank=True)
    statement=models.TextField()
    content=models.CharField(max_length=90,blank=True)
    user_who_attend=models.ManyToManyField(User,related_name='listOfUsers',null=True,blank=True)
    available=models.BooleanField(default=True)

    def is_expired(self):
        now= datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        event_time=datetime.strptime(str(self.events_date)[:19], "%Y-%m-%d %H:%M:%S")
        if now > event_time:
            
            return True
        return False
        
    def __str__(self) -> str:
        return self.name
    