import datetime as dt
import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Имя пользователя <me> недопустимо.')
    if not re.match(r'^[\w.@+-]+$', value):
        raise ValidationError(
            f'Недопустимые символы <{value}> в имени пользователя.')


def validate_title_year(value):
    year = dt.date.today().year
    if not (value <= year):
        raise ValidationError('Некоректный год.')
    return value
