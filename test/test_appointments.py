from datetime import date, datetime, timedelta

from appointments.appointments import main, new_event_with_alarm
from appointments.model.apps import App


def test_event_contains_alarm():
    actual = new_event_with_alarm(App("testtermin", date(1970, 1, 2)))
    assert 1 == len(actual.subcomponents)


def test_alarm_has_timezone():
    alarm = new_event_with_alarm(App("testtermin", date(1970, 1, 2))
                                 ).subcomponents[0]
    assert isinstance(alarm.decoded("TRIGGER"), datetime)


def test_alarm_is_localized():
    actual = (
        new_event_with_alarm(App("testtermin", date(1970, 1, 2)))
            .subcomponents[0]
            .decoded("TRIGGER")
    )
    assert actual.tzinfo is not None


def test_alarm_honors_dst():
    actual = (
        new_event_with_alarm(App("testtermin", date(2020, 10, 25)))
            .subcomponents[0]
            .decoded("TRIGGER")
    )

    assert actual.dst() == timedelta(0, 3600)


def test_alarm_honors_dst_in_winter():
    actual = (
        new_event_with_alarm(App("testtermin", date(2020, 10, 26)))
            .subcomponents[0]
            .decoded("TRIGGER")
    )

    assert actual.dst() == timedelta(0, 0)


def test_output_written_to_file(tmp_path):
    inputfile = tmp_path / "input.json"
    outputfile = tmp_path / "output.ics"

    with open(inputfile, "w") as file:
        file.write('[{"date": "2020-10-26", "type": "testtermin"}]')

    main(inputfile, outputfile)

    assert outputfile.exists()
