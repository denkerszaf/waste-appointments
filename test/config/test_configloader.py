from pathlib import Path

from appointments.config import json_input, toml_input
from appointments.config.configloader import ConfigLoader


def test_load_config(mocker):
    mocker.patch('appointments.config.json_input.load')
    mocker.patch('appointments.config.toml_input.load')
    ConfigLoader().load(Path('config.json'))

    json_input.load.assert_called_once_with(Path("config.json"))
    toml_input.load.assert_not_called()


def test_load_toml_config(mocker):
    mocker.patch('appointments.config.json_input.load')
    mocker.patch('appointments.config.toml_input.load')
    ConfigLoader().load(Path('config.toml'))

    toml_input.load.assert_called_once_with(Path("config.toml"))
    json_input.load.assert_not_called()
