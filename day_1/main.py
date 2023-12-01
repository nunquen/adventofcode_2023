from lib.utils import (
    get_local_data_as_list,
    # get_remote_data_as_list,
    LocalFile,
    # RemoteFile,
    validation_value_parser_part_1,
    validation_value_parser_part_2
)
from typing import List


def sum_calibration_values_part1(values: List):
    sum_values = 0
    for phrase in values:
        sum_values += validation_value_parser_part_1(phrase=phrase)

    return sum_values


def sum_calibration_values_part2(values: List):
    sum_values = 0
    for phrase in values:
        sum_values += validation_value_parser_part_2(phrase=phrase)

    return sum_values


if __name__ == "__main__":
    # input_file = RemoteFile.day1_input_file.value
    # values = get_remote_data_as_list(input_file=input_file)
    input_file = LocalFile.day1_input_file.value
    values = get_local_data_as_list(input_file=input_file)

    sum = sum_calibration_values_part1(values=values)
    print("Day #1. Calibration values part_1: {} ".format(sum))

    sum = sum_calibration_values_part2(values=values)
    print("Day #1. Calibration values part_2: {} ".format(sum))
