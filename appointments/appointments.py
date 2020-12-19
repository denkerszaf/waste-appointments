import datetime
import json

import tzlocal
from icalendar import Alarm, Calendar, Event


def new_alarm(alarmtime, description):
    alarm = Alarm()
    alarm.add("ACTION", "DISPLAY")
    alarm.add(
        "TRIGGER",
        alarmtime,
    )
    alarm.add("DESCRIPTION", description)

    return alarm


def new_event(appointment: dict) -> Event:
    event = Event()
    event.add("summary", appointment["type"])
    current_date = datetime.date.fromisoformat(appointment["date"])
    event.add("dtstart", current_date)
    # print('At', current_date, "bitte den", appointment['type'], "rausstellen.")

    return event


def new_event_with_alarm(appointment: dict) -> Event:
    event = new_event(appointment)
    alarmtime = tzlocal.get_localzone().localize(datetime.datetime(
        event.decoded("dtstart").year,
        event.decoded("dtstart").month,
        event.decoded("dtstart").day,
        19,
        00,
        tzinfo=None,
    ) - datetime.timedelta(days=1))

    event.add_component(
        new_alarm(alarmtime, " ".join([appointment["type"], "rausstellen"]))
    )

    return event


def main(inputfile, outputfile):
    with open(inputfile) as json_file:
        appointments = json.load(json_file)

    cal = Calendar()
    cal.add("prodid", "-//cal-generator//dn-kr.de//")
    cal.add("version", "0.5")

    for appointment in appointments:
        cal.add_component(new_event_with_alarm(appointment))

    with open(outputfile, "wb") as ical_file:
        ical_file.write(cal.to_ical())


if __name__ == "__main__":
    main("data/Papiermüll.json", "output.ics")
