
from rest_framework import serializers
from events.models import EventModel

class EventModelSerializer(serializers.ModelSerializer):
    user_who_attend=serializers.StringRelatedField(read_only=True,many=True)
    
    class Meta:
        model=EventModel
        fields='__all__'
