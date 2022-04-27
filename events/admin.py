from django.contrib import admin
from.models import EventModel, ImageModel,EventAlbumModel,VideoModel

# Register your models here.

admin.site.register(EventModel)

admin.site.register(ImageModel)

admin.site.register(EventAlbumModel)

admin.site.register(VideoModel)