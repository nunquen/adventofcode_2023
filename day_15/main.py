from lib.utils import (
    current_day,
    get_local_data_as_list,
    LocalFile,
    get_values
)

'''
--- Day 15: Lens Library ---
Reference: https://adventofcode.com/2023/day/15
'''


def test():
    input_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")
    value = get_values(phrases=input_data)

    assert value == 1320

    return True


if __name__ == "__main__":

    if not test():
        exit(1)

    print("Day {}. Tests passed!".format(current_day))

    print("Day {} Part1".format(current_day))
    input_file = LocalFile.day_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)
    values = get_values(phrases=input_data)
    print("Day {} Part1. Values for hashes: {}".format(
        current_day,
        values
    ))
