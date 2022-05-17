from django.contrib import admin

from .models import BookModel,ImageBookModel

# Register your models here.

admin.site.register(BookModel)  
admin.site.register(ImageBookModel)  