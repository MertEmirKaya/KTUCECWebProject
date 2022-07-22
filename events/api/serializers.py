from rest_framework import serializers
from events.models import EventModel,ImageModel,EventAlbumModel,VideoModel
from datetime import datetime


class ImageModelSerializer(serializers.ModelSerializer):
    image_path=serializers.SerializerMethodField()
    class Meta:
        model = ImageModel
        fields = ['image','image_path',]

    def get_image_path(self,obj):
        image=str(obj.image)
        # image_slash=image.find("/",3)
        # image_path=str(image[image_slash:])
        # print(image_slash)
        return image



class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoModel
        fields=['video']


class EventAlbumModelSerializer(serializers.ModelSerializer):
    images=ImageModelSerializer(many=True,read_only=True)
    videos=VideoModelSerializer(many=True,read_only=True)
    class Meta:
        model=EventAlbumModel
        fields=['images','videos']


class EventModelSerializer(serializers.ModelSerializer):
    
    album=EventAlbumModelSerializer(many=True,read_only=True)
    class Meta:
        model=EventModel
        fields='__all__'





