"""Date-related utilities."""
from datetime import date


def date_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)
