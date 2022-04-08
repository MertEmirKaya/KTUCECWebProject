
from rest_framework import serializers
from events.models import EventModel
from datetime import datetime
class EventModelSerializer(serializers.ModelSerializer):
    available=serializers.SerializerMethodField()
    class Meta:
        model=EventModel
        fields='__all__'


    def get_available(self,obj):
        now= datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        event_time=datetime.strptime(str(obj.events_date)[:19], "%Y-%m-%d %H:%M:%S")
        if now > event_time:
            
            return False
        return True