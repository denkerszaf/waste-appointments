import datetime
from pathlib import Path
from typing import List

import toml

from appointments.model.apps import App


def load(file: Path) -> List[App]:
    data = toml.load(file)

    result = list()
    if 'dates' in data.keys():
        appdates = data['dates']
        for (key, value) in appdates.items():
            result.append(App(description=value, date=datetime.date.fromisoformat(key)))
    return result
