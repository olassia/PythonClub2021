from django import forms
from .models import Meeting, MeetingMinute, Resource, Event

#Meeting & Resource

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'


class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'