"""Unit conversion helper functions."""

def convert_length(meters: float) -> dict:
    return {
        "公尺": meters,
        "公分": meters * 100,
        "公里": meters / 1000,
        "英吋": meters * 39.3701,
        "英呎": meters * 3.28084,
    }


def convert_weight(kg: float) -> dict:
    return {
        "公斤": kg,
        "公克": kg * 1000,
        "磅": kg * 2.20462,
        "盎司": kg * 35.274,
    }


def convert_temperature(celsius: float) -> dict:
    return {
        "攝氏": celsius,
        "華氏": celsius * 9 / 5 + 32,
        "開爾文": celsius + 273.15,
    }
