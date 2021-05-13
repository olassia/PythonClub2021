from django.contrib import admin
from .models import Meeting, MeetingMinute, Resource, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinute)
admin.site.register(Resource)
admin.site.register(Event)
