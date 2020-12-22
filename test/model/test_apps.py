from datetime import date

from appointments.model import apps

zero_epoch = date(1970, 1, 1)


def test_app_generation():
    actual = apps.App(description="test", date=zero_epoch)

    assert actual.description == 'test'
    assert actual.date == zero_epoch
    assert actual.version == 1
    assert actual.uid.startswith('1_0_test@')


def test_epoch_value():
    assert apps.epoch_value(date(1970, 1, 2)) == 86_400


def test_epoch_zero():
    assert apps.epoch_value(zero_epoch) == 0
