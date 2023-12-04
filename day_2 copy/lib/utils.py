from enum import Enum
from typing import List

debug = False


class LocalFile(Enum):
    day1_input_file = "day_2/input/values.txt"


class Game():
    def __init__(
        self,
        max_red_cubes: int,
        max_green_cubes: int,
        max_blue_cubes: int,
        line: str
    ) -> None:
        self._number = int(line.split(":")[0].split()[1])
        self._is_valid, self._is_valid_part2, self._game, self._few_cubes = Game.feed(
            sets=line.split(":")[1],
            max_red_cubes=max_red_cubes,
            max_green_cubes=max_green_cubes,
            max_blue_cubes=max_blue_cubes
        )

    @staticmethod
    def feed(
        sets: str,
        max_red_cubes: int,
        max_green_cubes: int,
        max_blue_cubes: int,
    ) -> (bool, bool, List, dict):
        is_valid = True
        is_valid_part2 = True
        game = []
        few_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }

        for current_set in sets.split(";"):
            cubes = {
                "red": 0,
                "blue": 0,
                "green": 0
            }

            # Part1
            for color in current_set.split(","):
                cubes["red"] = int(color.strip().split()[0]) if "red" in color else cubes["red"]
                cubes["green"] = int(color.strip().split()[0]) if "green" in color else cubes["green"]
                cubes["blue"] = int(color.strip().split()[0]) if "blue" in color else cubes["blue"]

            is_valid = is_valid and cubes["red"] <= max_red_cubes and \
                cubes["green"] <= max_green_cubes and \
                cubes["blue"] <= max_blue_cubes

            # Part2
            few_cubes["red"] = cubes["red"] if cubes["red"] > few_cubes["red"] else few_cubes["red"]
            few_cubes["green"] = cubes["green"] if cubes["green"] > few_cubes["green"] else few_cubes["green"]
            few_cubes["blue"] = cubes["blue"] if cubes["blue"] > few_cubes["blue"] else few_cubes["blue"]

            game.append(cubes)

        min_cubes = min(max_red_cubes, max_green_cubes, max_blue_cubes)

        is_valid_part2 = few_cubes["red"] + few_cubes["green"] + few_cubes["blue"] >= min_cubes

        return is_valid, is_valid_part2, game, few_cubes


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


def get_games_from_data(
    data: List,
    max_cubes: dict
) -> (int, List):
    games = []
    valid_games_counter = 0
    valid_games_counter_part2 = 0

    for line in data:
        game = Game(
            line=line,
            max_red_cubes=max_cubes["red"],
            max_green_cubes=max_cubes["green"],
            max_blue_cubes=max_cubes["blue"]
        )
        valid_games_counter += game._number if game._is_valid else 0
        valid_games_counter_part2 += \
            (
                game._few_cubes["red"] *
                game._few_cubes["green"] *
                game._few_cubes["blue"]
            ) \
            if game._is_valid_part2 else 0

        games.append(game)

    return valid_games_counter, valid_games_counter_part2, games
