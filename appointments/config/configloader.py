from pathlib import Path

from appointments.config import json_input, toml_input


class ConfigLoader:

    def load(self, file: Path):
        if file.suffix == ".toml":
            return toml_input.load(file)
        else:
            return json_input.load(file)
