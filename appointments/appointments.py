import datetime

import tzlocal
from icalendar import Alarm, Calendar, Event

from appointments.config import json_input
from appointments.model.apps import App


def new_alarm(alarmtime, description):
    alarm = Alarm()
    alarm.add("ACTION", "DISPLAY")
    alarm.add(
        "TRIGGER",
        alarmtime,
    )
    alarm.add("DESCRIPTION", description)

    return alarm


def new_event(appointment: App) -> Event:
    event = Event()
    event.add("summary", appointment.description)
    event.add("dtstart", appointment.date)

    return event


def new_event_with_alarm(appointment: App) -> Event:
    event = new_event(appointment)
    alarmtime = tzlocal.get_localzone().localize(datetime.datetime(
        appointment.date.year,
        appointment.date.month,
        appointment.date.day,
        19,
        0,
        tzinfo=None,
    ) - datetime.timedelta(days=1))

    event.add_component(
        new_alarm(alarmtime, " ".join([appointment.description, "rausstellen"]))
    )

    return event


def main(inputfile, outputfile):
    appointments = json_input.load(inputfile)

    cal = Calendar()
    cal.add("prodid", "-//cal-generator//dn-kr.de//")
    cal.add("version", "0.5")

    for appointment in appointments:
        cal.add_component(new_event_with_alarm(appointment))

    with open(outputfile, "wb") as ical_file:
        ical_file.write(cal.to_ical())


if __name__ == "__main__":
    main("data/Papiermüll.json", "output.ics")
