from rest_framework import serializers
from books.models import BookModel,ImageBookModel

class ImageBookSerializer(serializers.ModelSerializer):

    class Meta:
        model=ImageBookModel
        fields=('image',)

class BookModelSerializer(serializers.ModelSerializer):
    images=ImageBookSerializer(many=True,read_only=True)
    available=serializers.SerializerMethodField()
    class Meta:
        model=BookModel
        exclude=['date_of_giving','user_who_got']


    def get_available(self,obj):
        if obj.user_who_got is not None:
            return False

        return True    
