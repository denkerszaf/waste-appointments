import datetime
import json

from icalendar import Alarm, Calendar, Event

with open("data/Papiermüll.json") as json_file:
    appointments = json.load(json_file)

cal = Calendar()
cal.add("prodid", "-//cal-generator//dn-kr.de//")
cal.add("version", "0.5")

for appointment in appointments:
    event = Event()
    event.add("summary", appointment["type"])
    current_date = datetime.date.fromisoformat(appointment["date"])
    event.add("dtstart", current_date)
    # print('At', current_date, "bitte den", appointment['type'], "rausstellen.")

    alarm = Alarm()
    alarm.add("ACTION", "DISPLAY")
    alarm.add(
        "TRIGGER",
        datetime.datetime(
            current_date.year, current_date.month, current_date.day, 19, 00
        )
        - datetime.timedelta(days=1),
    )
    alarm.add("DESCRIPTION", " ".join([appointment["type"], "rausstellen"]))
    event.add_component(alarm)

    cal.add_component(event)

with open("output.ics", "wb") as ical_file:
    ical_file.write(cal.to_ical())
# print(cal.to_ical()
