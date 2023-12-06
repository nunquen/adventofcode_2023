from lib.utils import (
    get_best_times,
    get_the_number
)

'''
Reference: https://adventofcode.com/2023/day/6
'''


def test():
    res = True
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

    input_data_part2 = {
            "Time": 71530,
            "Distance": 940200,
        }

    assert get_the_number(input_data=input_data) == 288

    # Part2
    best_times = get_best_times(
        time=input_data_part2["Time"],
        distance=input_data_part2["Distance"]
    )
    assert len(best_times) == 71503

    return res


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

    input_data_part2 = {
            "Time": 41968894,
            "Distance": 214178911271055,
        }

    the_number = get_the_number(input_data=input_data)

    print("Day #6. Multiply the ways I can beat the record: {} ".format(
        the_number
        )
    )

    # Part2
    best_times = get_best_times(
        time=input_data_part2["Time"],
        distance=input_data_part2["Distance"]
    )
    print("Day #6. All possible ways for record beating (part2): {} ".format(
        len(best_times)
        )
    )
