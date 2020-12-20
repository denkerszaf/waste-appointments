import datetime
import json
from pathlib import Path
from typing import List

from appointments.model.apps import App


def load(file: Path) -> List[App]:
    with open(file) as json_file:
        appointments = json.load(json_file)
    return [App(description=x['type'], date=datetime.date.fromisoformat(x['date'])) for x in appointments]
