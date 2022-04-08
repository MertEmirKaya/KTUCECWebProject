from rest_framework import generics,filters
from books.models import BookModel
from .serializers import BookModelSerializer


class BookModelListAPIView(generics.ListAPIView):
    queryset=BookModel.objects.filter(available=True)
    serializer_class=BookModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content','author']

class BookModelDetailAPIView(generics.RetrieveAPIView):
    queryset=BookModel.objects.filter(available=True)
    serializer_class=BookModelSerializer
    lookup_field='title'    