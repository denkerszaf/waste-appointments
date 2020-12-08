import datetime
import json

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


def main():
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

        alarmtime = datetime.datetime(
            current_date.year, current_date.month, current_date.day, 19, 00
        ) - datetime.timedelta(days=1)

        event.add_component(
            new_alarm(alarmtime, " ".join([appointment["type"], "rausstellen"]))
        )

        cal.add_component(event)

    with open("output.ics", "wb") as ical_file:
        ical_file.write(cal.to_ical())


if __name__ == "__main__":
    main()
