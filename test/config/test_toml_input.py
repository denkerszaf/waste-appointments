from pathlib import Path

from appointments.config.toml_input import load
from appointments.model.apps import App


def test_empty_file(tmp_path: Path) -> None:
    file = write_content(tmp_path, "version = 2")

    actual = load(file)
    assert len(actual) == 0


def test_single_item(tmp_path: Path) -> None:
    file = write_content(tmp_path, "version = 2\n", "[Wertstoff]\n", "dates = [ 2020-01-04 ]\n")
    actual = load(file)

    assert isinstance(actual[0], App)


def write_content(tmp_path: Path, *args) -> Path:
    file = tmp_path / "input"
    with open(file, "w") as fh:
        fh.writelines(args)
    return file
