from lib.utils import (
    get_best_times,
    get_the_number
)

'''
Reference: https://adventofcode.com/2023/day/6
'''


def test():

    input_data = [
        {
            "Time": 7,
            "Distance": 9,
        },
        {
            "Time": 15,
            "Distance": 40,
        },
        {
            "Time": 30,
            "Distance": 200,
        },
    ]

    return get_the_number(input_data=input_data) == 288


if __name__ == "__main__":

    if not test():
        exit(1)

    input_data = [
        {
            "Time": 41,
            "Distance": 214,
        },
        {
            "Time": 96,
            "Distance": 1789,
        },
        {
            "Time": 88,
            "Distance": 1127,
        },
        {
            "Time": 94,
            "Distance": 1055,
        },
    ]
    the_number = get_the_number(input_data=input_data)

    print("Day #6. Multiply the ways I can beat the record: {} ".format(
        the_number
        )
    )
