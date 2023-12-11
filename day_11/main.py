from lib.utils import (
    get_local_data_as_list,
    LocalFile,
    expand_universe,
    rename_galaxies,
    get_pairs,
    calculate_path_steps
)

'''
--- Day 11: Haunted Wasteland ---
Reference: https://adventofcode.com/2023/day/11
'''


def test():
    input_data = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]

    universe = expand_universe(universe=input_data)
    universe, galaxies = rename_galaxies(universe=universe)
    pairs = get_pairs(galaxies=galaxies)
    steps = 0
    for pair in pairs:
        step = calculate_path_steps(
            universe=universe,
            galaxy1=pair[0],
            galaxy2=pair[1]
        )

        steps += step

    return steps == 374


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)

    universe = expand_universe(universe=input_data)
    universe, galaxies = rename_galaxies(universe=universe)
    pairs = get_pairs(galaxies=galaxies)
    steps = 0
    for pair in pairs:
        step = calculate_path_steps(
            universe=universe,
            galaxy1=pair[0],
            galaxy2=pair[1]
        )

        steps += step

    print("Day 11. Steps to reach destination. Part1. Value: {} ".format(
        steps
        )
    )
