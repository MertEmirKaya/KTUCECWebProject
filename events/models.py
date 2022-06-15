from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return f'events/{instance.album}/{filename}'

class EventModel(models.Model):

    name=models.CharField(max_length=100,)
    organizer=models.CharField(max_length=100,blank=True,null=True)
    events_date=models.DateTimeField()
    announcement_date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=100,blank=True)
    statement=models.TextField()
    content=models.CharField(max_length=90,blank=True)
    is_ready=models.BooleanField(default=False,)



    def __str__(self) -> str:
        return str(self.name)
    

class EventAlbumModel(models.Model):

    event=models.ForeignKey(EventModel,on_delete=models.CASCADE,related_name='album',null=True,blank=True)
    

    def __str__(self) -> str:
        return str(self.event)+' event album'


class ImageModel(models.Model):
   
    album=models.ForeignKey(EventAlbumModel,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(null=True,blank=True,upload_to=upload_to)
    
    def __str__(self) -> str:
        return str(self.album)+' event image'

class VideoModel(models.Model):
 
    album=models.ForeignKey(EventAlbumModel,on_delete=models.CASCADE,related_name='videos')
    video=models.FileField(upload_to=upload_to)

    def __str__(self) -> str:
        return str(self.album)+' event video'    