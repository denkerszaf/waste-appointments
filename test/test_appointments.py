#!/bin/python3

from waste_appointments.appointsments import new_alarm


def test_alarm_generation():
    assert new_alarm()
