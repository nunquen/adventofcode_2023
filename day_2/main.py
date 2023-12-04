from lib.utils import (
    get_local_data_as_list,
    get_games_from_data,
    LocalFile,
)
from typing import List


def sum_cube_conondrum_part1(values: List):
    sum_valid_games = 0
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum_valid_games, valid_games_counter_part2, games = get_games_from_data(
        data=values,
        max_cubes=max_cubes
    )

    return sum_valid_games, valid_games_counter_part2, games


if __name__ == "__main__":
    input_file = LocalFile.day1_input_file.value
    games = get_local_data_as_list(input_file=input_file)

    valid_ones, valid_ones_part2, sum = sum_cube_conondrum_part1(values=games)
    print("Day #2. Cube conondrum sum IDs part 1. Valid games: {} ".format(valid_ones))
    print("Day #2. Cube conondrum sum IDs part 2. Valid games: {} ".format(valid_ones_part2))
