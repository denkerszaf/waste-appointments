#!/usr/bin/python

import tzlocal
import requests
import datetime
from icalendar import Alarm, Calendar, Event, vDDDTypes

def create_alarm(time: vDDDTypes):
   alarmtime = tzlocal.get_localzone().localize(datetime.datetime( time.dt.year, time.dt.month, time.dt.day, 19,0,tzinfo=None) - datetime.timedelta(days=1))
   alarm = Alarm()
   alarm.add("ACTION", "DISPLAY")
   alarm.add("TRIGGER", alarmtime)
   return alarm


r = requests.get(
    "https://www.blauetonne-schlauetonne.de/abfuhrkalender/2022/pfinztal-woeschbach-kleinsteinbach-285.ics");

calendar = Calendar.from_ical(r.content);
for event in calendar.walk('vevent'):
    del event['DTEND']
    event.subcomponents = [ sc for sc in event.subcomponents if type(sc) != 'icalendar.cal.Alarm' ] # delete all alarms
    event.add_component(create_alarm(event['DTSTART']))
    event['DTSTART'].dt = event['DTSTART'].dt.date()

print(calendar.to_ical().decode('UTF-8'))

