from datetime import date
from urllib.parse import quote

zero = date(1970, 1, 1)


class App:

    def __init__(self, description: str, date: date):
        self.description = description
        self.date = date
        self.version = 1

        self.uid = f'{self.version}_{epoch_value(self.date)}_{quote(self.description)}@waste-appointments.scripts.dn-kr.de'


def epoch_value(d: date) -> int:
    delta_d = d - zero
    return int(delta_d.total_seconds())
