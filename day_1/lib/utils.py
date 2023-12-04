from enum import Enum
from typing import List
import re
import urllib3


debug = False

number_list = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
    ["nine", "9"]
]


class RemoteFile(Enum):
    day1_input_file = "https://adventofcode.com/2023/day/1/input"


class LocalFile(Enum):
    day1_input_file = "day_1/input/values.txt"


def get_remote_data_as_list(input_file: str) -> List:
    content = []

    data = urllib3.urlopen(input_file)
    for line in data:
        content.append(line)

    return content


def get_local_data_as_list(input_file: str) -> List:
    content = []
    try:
        local_file = open(input_file, "r")
        for line in local_file.readlines():
            content.append(line.rstrip("\n"))
    except Exception as e:
        print("Error while reading file {}. The error:\n{}".format(
            input_file,
            str(e)
        ))

    return content


def validation_value_parser_part_1(phrase: str) -> int:
    first_value = ""
    last_value = ""
    value = 0

    match = re.search(r"\d", phrase)
    if match:
        first_value = match.group()

    match2 = re.search(r"\d", phrase[::-1]).group()[::-1]
    if match2:
        last_value = match2

    value = int(first_value + last_value)
    if debug:
        print("value is: {}".format(value))

    return value


def validation_value_parser_part_2(phrase: str) -> int:
    first_value = ""
    first_value_index = -1
    last_value = ""
    last_value_index = -1
    value = 0

    # Looking for the first numeric number in the phrase
    match = re.search(r"\d", phrase)
    if match:
        first_value = match.group()
        first_value_index = match.start()

    # Lookling for the first numeric name in the phrase
    for number in number_list:
        number_index = phrase.find(number[0])
        if number_index > -1 and number_index < first_value_index:
            first_value_index = number_index
            first_value = number[1]

    # Looking for the last numeric number in the phrase
    match2 = re.search(r"\d", phrase[::-1])
    if match2:
        last_value = match2.group()[::-1]
        last_value_index = len(phrase) - match2.start() - 1

    # Lookling for the last numeric name in the phrase
    for number in number_list:
        number_index = phrase[::-1].find(number[0][::-1])
        if number_index == -1:
            continue

        number_index = len(phrase) - len(number[0]) - number_index

        if number_index > -1 and number_index > last_value_index:
            last_value_index = number_index
            last_value = number[1]

    value = int(first_value + last_value)
    if debug:
        print("value is: {}".format(value))

    return value
