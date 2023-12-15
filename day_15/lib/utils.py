from enum import Enum
from typing import List


debug = False
current_day = 15


class LocalFile(Enum):
    day_input_file = "day_{}/input/values.txt".format(current_day)


def get_local_data_as_list(input_file: str) -> List:
    content = []
    try:
        local_file = open(input_file, "r")
        for line in local_file.readlines():
            content = line.rstrip("\n").split(",")
            break
    except Exception as e:
        print("Error while reading file {}. The error:\n{}".format(
            input_file,
            str(e)
        ))

    return content


def hash_algorithm(phrase: str) -> int:
    value = 0
    multiplier = 17
    divider = 256

    for letter in phrase:
        value += ord(letter)
        value = (value * multiplier) % divider

    return value


def get_values(phrases: List[str]) -> int:
    value = 0
    for phrase in phrases:
        value += hash_algorithm(phrase=phrase)

    return value
