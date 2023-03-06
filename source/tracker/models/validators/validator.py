from django.core.exceptions import ValidationError
import re


def tracker_summary_validator(name):
    regex = re.findall(r'[^a-zA-Z0-9\s]', name)
    for reg in regex:
        if reg in name:
            raise ValidationError("В наименовании задачи не должно быть спецсимволов!")
    return name

def tracker_description_validator(name):
    if len(name) < 15:
        raise ValidationError("Описание задачи должно состоять не менее чем из 15 символов")
    return name