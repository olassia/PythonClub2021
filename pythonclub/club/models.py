from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingname=models.CharField(max_length=255)
    meetingdescription=models.TextField(null=True, blank=True)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.TextField(null=True, blank=True)
    meetingagenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingname

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinute(models.Model):
    meetingminute=models.CharField(max_length=255)
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingminute

    class Meta:
        db_table='meetingminute'
        verbose_name_plural='meetingminutes'


#Meeting Minutes which will have fields for meeting id (a foreign key), 
#attendance (a many to many field with User), Minutes text


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField(null=True, blank=True)
    url=models.URLField(null=True, blank=True)
    entrydate=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'


#Resource which will have fields for resource name, resource type, URL, 
# date entered, user id (foreign key with User), and description



class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField(null=True, blank=True)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'
        verbose_name_plural='events'


#Event which will have fields for event title, location, date, time, 
# description and the user id of the member that posted it