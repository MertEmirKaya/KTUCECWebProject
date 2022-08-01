from rest_framework import generics
from .serializers import EventModelSerializer
from events.models import EventModel
import datetime
from rest_framework.pagination import PageNumberPagination
now= datetime.datetime.now()

class UpComingEventModelListAPIView(generics.ListAPIView):
    queryset=EventModel.objects.filter(is_ready=True,events_date__gt=now)
    serializer_class=EventModelSerializer    

class PastEventModelListAPIView(generics.ListAPIView):
    queryset=EventModel.objects.filter(is_ready=True,)
    serializer_class=EventModelSerializer   
    pagination_class=PageNumberPagination

class EventModelDetailAPIView(generics.RetrieveAPIView):

   
    queryset=EventModel.objects.filter(is_ready=True)
    serializer_class=EventModelSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



