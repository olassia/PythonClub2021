from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.name=Meeting(meetingname='Meeting1', meetingdescription='basic Python', 
        meetingdate=datetime.date(2021,5,28), meetingtime=datetime.time(hour=6, minute=30), 
        meetinglocation='Seattle, WA 98108', meetingagenda='basic Python')

    def test_namestring(self):
        self.assertEqual(str(self.name), 'Meeting1')    

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')
  

class MeetingMinuteTest(TestCase):
    def setUp(self):
        self.name=Meeting(meetingname='Meeting1')
        self.attendance=User(username='Nicholas')
        self.minute=MeetingMinute(meetingminute='Meeting Min', 
        attendance=self.attendance, minutestext='Minute text')

    def test_minutetring(self):
        self.assertEqual(str(self.meetingminute), 'Meeting Min')            

class ResourceTest(TestCase):
    def setUp(self):
        self.userid=User(username='Nicholas')
        self.name=Resource(resourcename='Python Beginner Guide', resourcetype='Wiki Python links', 
        url='https://wiki.python.org/moin/BeginnersGuide/Programmers', entrydate=datetime.date(2021,5,15), 
        userid=self.userid, description='Basics to Python.')

    def test_namestring(self):
        self.assertEqual(str(self.name), 'Python Beginner Guide')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')    


class EventTest(TestCase):
    def setUp(self):
        self.userid=User(username='Nicholas')
        self.title=Event(eventtitle='Seattle Python 101', eventlocation='Seattle, WA', 
        eventtime=datetime.time(hour=12, minute=00), userid=self.userid)

    def test_titlestring(self):
        self.assertEqual(str(self.title), 'Seattle Python 101')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

    def test_locationstring(self):
        self.assertEqual(str(self.eventlocation), 'Seattle, WA')                                              