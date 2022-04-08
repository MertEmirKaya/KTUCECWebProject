from rest_framework import generics
from .serializer import EventModelSerializer
from events.models import EventModel
from rest_framework import status
from rest_framework.response import Response


class EventModelListAPIView(generics.ListAPIView):
    queryset=EventModel.objects.all()
    serializer_class=EventModelSerializer    


class EventModelDetailAPIView(generics.RetrieveAPIView):

    lookup_field = "name"
    queryset=EventModel.objects.all()
    serializer_class=EventModelSerializer

    def retrieve(self, request, *args, **kwargs):
        name=self.kwargs.get('name')
        event=EventModel.objects.get(name=name)
        
        if event.is_expired():
            EventModel.objects.filter(name=name).update(available=False)
            

        return super().retrieve(request, *args, **kwargs)



