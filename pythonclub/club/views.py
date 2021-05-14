from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

   
