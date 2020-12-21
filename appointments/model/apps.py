from datetime import date


class App:

    def __init__(self, description: str, date: date):
        self.description = description
        self.date = date

    def __eq__(self, other) -> bool:
        return self.date == other.date and self.description == other.description
