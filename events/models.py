from django.db import models
import uuid
# Create your models here.

def upload_to(instance, filename):
    album_path=str(instance.album).replace(" ","")
    filename=str(filename).replace(" ","")
    return f'events/{album_path}/{filename}'

class EventModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name=models.CharField(max_length=100,)
    organizer=models.CharField(max_length=100,blank=True,null=True)
    events_date=models.DateTimeField()
    announcement_date=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=100,blank=True)
    statement=models.TextField()
    content=models.CharField(max_length=90,blank=True)
    is_ready=models.BooleanField(default=False,)
    application_url=models.URLField(max_length=200,null=True,blank=True)


    def __str__(self) -> str:
        return str(self.name)
    

class EventAlbumModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    event=models.ForeignKey(EventModel,on_delete=models.CASCADE,related_name='album',null=True,blank=True)
    

    def __str__(self) -> str:
        return str(self.event)+' event album'


class ImageModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    album=models.ForeignKey(EventAlbumModel,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(null=True,blank=True,upload_to=upload_to)
    
    def __str__(self) -> str:
        return "event image of"+ str(self.album)

class VideoModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    album=models.ForeignKey(EventAlbumModel,on_delete=models.CASCADE,related_name='videos')
    video=models.FileField(upload_to=upload_to)

    def __str__(self) -> str:

        return "event video of"+ str(self.album)   