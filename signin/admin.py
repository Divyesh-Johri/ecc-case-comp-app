from django.contrib import admin

# Register your models here.

from . import models

class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Announcements, AnnouncementsAdmin)