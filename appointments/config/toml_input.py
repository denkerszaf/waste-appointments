from pathlib import Path
from typing import List

import toml

from appointments.model.apps import App


def load(file: Path) -> List[App]:
    data = toml.load(file)

    result = list()
    for (key, value) in data.items():
        if type(value) is dict:
            for date in value['dates']:
                result.append(App(description=key, date=date))
    return result
