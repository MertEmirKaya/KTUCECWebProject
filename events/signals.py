from django.db.models import signals
from django.dispatch import receiver
from .models import EventModel ,EventAlbumModel

@receiver(signals.post_save,sender=EventModel)
def create_event(sender,instance,created,**kwargs):
    EventAlbumModel.objects.create(event=instance)