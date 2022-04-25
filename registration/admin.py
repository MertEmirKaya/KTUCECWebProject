from django.contrib import admin
from .models import ProfileModel
# Register your models here.

class ProfileModelAdmin(admin.ModelAdmin):
    list_display =('username',)
    list_filter=('fee',)
    search_fields=('username','bio')
    ordering = ('username',)

admin.site.register(ProfileModel,ProfileModelAdmin)