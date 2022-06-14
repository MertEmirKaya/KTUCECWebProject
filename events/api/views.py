from rest_framework import generics
from .serializers import EventModelSerializer
from events.models import EventModel



class EventModelListAPIView(generics.ListAPIView):
    queryset=EventModel.objects.filter(is_ready=True)
    serializer_class=EventModelSerializer    


class EventModelDetailAPIView(generics.RetrieveAPIView):

   
    queryset=EventModel.objects.filter(is_ready=True)
    serializer_class=EventModelSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



