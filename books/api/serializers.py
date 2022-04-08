from rest_framework import serializers
from books.models import BookModel
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        exclude=['date_of_giving','user_who_got']