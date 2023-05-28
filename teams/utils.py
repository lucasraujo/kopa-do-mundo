from .exceptions import NegativeTitlesError
from .exceptions import InvalidYearCupError, ImpossibleTitlesError


def data_processing(data):
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_year = int(data["first_cup"].split("-")[0])
    titles = int(data["titles"])

    if first_cup_year < 1930 or (1930 - first_cup_year) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    cupUntilToday = []
    for year in range(first_cup_year, 2023, 4):
        cupUntilToday.append(year)

    if int(data["titles"]) > len(cupUntilToday):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
