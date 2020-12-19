import random
import string

from appointments.json_input import load


def test_empty_list(tmp_path):
    file = write_content(tmp_path, "[]")
    result = load(file)

    assert len(result) == 0


def test_single_item(tmp_path):
    file = write_content(tmp_path, '[{"date": "2020-01-03", "type": "Papiermüll"}]')

    result = load(file)

    assert len(result) == 1
    appointment = result[0]
    assert appointment.description == "Papiermüll"
    assert appointment.date.year == 2020
    assert appointment.date.month == 1
    assert appointment.date.day == 3


def write_content(tmp_path, content):
    chars = string.ascii_letters + string.digits
    filename = ''.join(random.choice(chars) for i in range(20))
    file = tmp_path / filename

    with open(file, 'w') as fh:
        fh.write(content)

    return file
