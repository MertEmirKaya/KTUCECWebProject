
from email.mime import image
from rest_framework import serializers
from events.models import EventModel,ImageModel,EventAlbumModel,VideoModel
from datetime import datetime
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ImageModelSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
        ]
    )

    class Meta:
        model = ImageModel
        fields = ['image',]

   


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
    is_expired=serializers.SerializerMethodField()
    album=EventAlbumModelSerializer(many=True,read_only=True)
    class Meta:
        model=EventModel
        fields='__all__'


    def get_is_expired(self,obj):
        now= datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        event_time=datetime.strptime(str(obj.events_date)[:19], "%Y-%m-%d %H:%M:%S")
        if now > event_time:
            
            return True
        return False


