from datetime import datetime
from appointments import new_event_with_alarm


def test_alarm_generation():
    assert True


def test_event_contains_alarm():
    actual = new_event_with_alarm({"date": "1970-01-02", "type": "testtermin"})
    assert 1 == len(actual.subcomponents)


def test_alarm_has_timezone():
    alarm = new_event_with_alarm(
        {"date": "1970-01-02", "type": "testtermin"}
    ).subcomponents[0]
    assert isinstance(alarm.decoded("TRIGGER"), datetime)


def test_alarm_is_localized():
    actual = (
        new_event_with_alarm({"date": "1970-01-02", "type": "testtermin"})
        .subcomponents[0]
        .decoded("TRIGGER")
    )
    assert actual.tzinfo is not None
