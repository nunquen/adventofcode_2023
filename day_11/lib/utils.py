import itertools
import numpy as np
from enum import Enum
from typing import List, Tuple

debug = False


class LocalFile(Enum):
    day_input_file = "day_11/input/values.txt"


class Galaxy(Enum):
    character = "#"


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


def transpose(l1):
    l2 = []
    # Convert string to list of characters
    for i in range(len(l1)):
        l2.append(list(l1[i]))
    # Transposing
    l2 = np.array(l2).T.tolist()
    return l2


def get_pairs(galaxies: int) -> List[tuple]:
    all_galaxies = list(range(galaxies+1))[1:]

    combinations = list(itertools.combinations(all_galaxies, 2))

    return combinations


def expand_universe(
    universe: List[str],
    expansion: int = 1
):
    new_universe = []
    # Expand rows
    for num in range(len(universe)):
        new_universe.append(universe[num])
        if Galaxy.character.value not in universe[num]:
            # Part2: expand the universe more and more...
            if expansion == 1:
                new_universe.append(universe[num])
                continue

            # for expansion_index in range(expansion-1):
            #     new_universe.append(universe[num])
            new_universe += [universe[num]] * (expansion - 1)

    # Transpose rows with columns
    universe = transpose(
        l1=new_universe
    )
    new_universe = []
    # Expand rows
    for num in range(len(universe)):
        new_universe.append(universe[num])
        if Galaxy.character.value not in universe[num]:
            # Part2: expand the universe more and more...
            if expansion == 1:
                new_universe.append(universe[num])
                continue

            # for expansion_index in range(expansion-1):
            #     new_universe.append(universe[num])
            new_universe += [universe[num]] * (expansion - 1)

    # Flipping back again the entire universe
    universe = transpose(
        l1=new_universe
    )

    new_universe = None
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
    galaxy2: int
) -> int:
    galaxy1_position = get_position(universe=universe, galaxy_name=galaxy1)
    galaxy2_position = get_position(universe=universe, galaxy_name=galaxy2)

    steps = abs(galaxy1_position[0] - galaxy2_position[0]) + \
        abs(galaxy1_position[1] - galaxy2_position[1])

    return steps
