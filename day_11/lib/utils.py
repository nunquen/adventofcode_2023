import itertools
import numpy as np
from enum import Enum
from typing import List, Tuple

debug = False


class LocalFile(Enum):
    day_input_file = "day_11/input/values.txt"


class Galaxy(Enum):
    character = "#"
    empty_space = "E"


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


def transpose(l1: List):
    l2 = []
    # Convert string to list of characters
    if isinstance(l1[1], str):
        for i in range(len(l1)):
            l2.append(list(l1[i]))

    # Transposing
        l3 = np.array(l2).T.tolist()
        l2 = None
        return l3
    else:
        l2 = np.array(l1).T.tolist()

    l1 = None
    return l2


def get_pairs(galaxies: int) -> List[tuple]:
    all_galaxies = list(range(galaxies+1))[1:]

    combinations = list(itertools.combinations(all_galaxies, 2))

    return combinations


def prepare_universe(universe: List[str]) -> List[List]:
    new_universe = []
    for num in range(len(universe)):
        if isinstance(universe[num], str):
            new_universe.append(list(universe[num]))

    return new_universe


def expand_universe(
    universe: List[str],
    expansion: int = 1
):
    new_universe = []
    # Expand rows
    for num in range(len(universe)):
        if Galaxy.character.value not in universe[num]:
            # Part2: expand the universe more and more...
            new_universe.append(
                [s.replace(
                    ".",
                    "E{}".format(expansion + 1)) for s in universe[num]]
            )
        else:
            new_universe.append(universe[num])

    # Transpose rows with columns
    flipped_universe = transpose(
        l1=new_universe
    )
    new_universe = []
    # Expand rows
    for num in range(len(flipped_universe)):
        if Galaxy.character.value not in flipped_universe[num]:
            # Part2: expand the flipped_universe more and more...
            new_universe.append(
                [s.replace(
                    ".",
                    "E{}".format(expansion + 1)) for s in flipped_universe[num]]
            )
        else:
            new_universe.append(flipped_universe[num])

    # Flipping back again the entire universe
    universe = transpose(
        l1=new_universe
    )

    new_universe = None
    flipped_universe = None
    return universe


def get_position(
    universe: List,
    galaxy_name: int,
) -> Tuple[int, int]:
    return next((i, j) for i, lst in enumerate(universe)
                for j, x in enumerate(lst) if x == galaxy_name)


def rename_galaxies(universe: List) -> (List, int):
    galaxy_name = 1
    for num in range(len(universe)):
        if Galaxy.character.value not in universe[num]:
            continue

        for index in range(len(universe[num])):
            if universe[num][index] == Galaxy.character.value:
                universe[num][index] = galaxy_name
                galaxy_name += 1

    return galaxy_name - 1


def calculate_path_steps(
    universe: List,
    galaxy1: int,
    galaxy2: int,
    expansion: int = 1
) -> int:
    galaxy1_position = get_position(universe=universe, galaxy_name=galaxy1)
    galaxy2_position = get_position(universe=universe, galaxy_name=galaxy2)

    # Part2: empty space is in cells begginging with E.
    #        Ex: E4 means 4 empty spaces
    empty_space_in_rows = 0
    min_row_position = min(galaxy1_position[0], galaxy2_position[0])
    max_row_position = max(galaxy1_position[0], galaxy2_position[0])
    for num in range(max_row_position - min_row_position):
        # Check if the entire row holds expanded space
        times = universe[min_row_position + num + 1].count(
            "{}{}".format(
                Galaxy.empty_space.value,
                expansion + 1
            )
        )
        if times == len(universe[min_row_position + num + 1]):
            empty_space_in_rows += 1

    # Calculating expanded empty space between columns
    min_col_position = min(galaxy1_position[1], galaxy2_position[1])
    max_col_position = max(galaxy1_position[1], galaxy2_position[1])
    empty_space_btwn_cols = universe[0][
            min_col_position:max_col_position
        ].count(
            "E{}".format(expansion + 1)
        )
    expansion = expansion - 1 if expansion > 1 else expansion
    steps = (max_row_position - min_row_position + empty_space_in_rows * expansion) + \
        max_col_position - min_col_position + empty_space_btwn_cols * expansion

    return steps
