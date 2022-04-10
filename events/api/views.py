from rest_framework import generics
from .serializer import EventModelSerializer
from events.models import EventModel
from rest_framework import status
from rest_framework.response import Response


class EventModelListAPIView(generics.ListAPIView):
    queryset=EventModel.objects.filter(is_ready=True)
    serializer_class=EventModelSerializer    


class EventModelDetailAPIView(generics.RetrieveAPIView):

    lookup_field = "name"
    queryset=EventModel.objects.all()
    serializer_class=EventModelSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



