import json


def load(file: str) -> set:
    with open(file) as json_file:
        appointments = json.load(json_file)
    return appointments
