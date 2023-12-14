import numpy as np
from enum import Enum
from typing import List, Tuple
import copy

debug = False
current_day = 14


class LocalFile(Enum):
    day_input_file = "day_{}/input/values.txt".format(current_day)


class DishObject(Enum):
    round_rock = "O"
    cube_rock = "#"
    empty_space = "."


# Part2
class Direction(Enum):
    north = "N"
    west = "W"
    south = "S"
    east = "E"


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


def prepare_data(data: List[str]) -> List[List]:
    new_data = []
    for num in range(len(data)):
        if isinstance(data[num], str):
            new_data.append(list(data[num]))

    return new_data


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


def get_position(
    area: List,
    target: int,
) -> Tuple[int, int]:
    return next((i, j) for i, lst in enumerate(area)
                for j, x in enumerate(lst) if x == target)


def list_to_string(l1: List) -> str:
    string_list = [str(element) for element in l1]
    return "".join(string_list)


def move_to_the_left(section: str):
    # Replacing ".O" with "O."" will move one round rock to the left
    section = section.replace(
       DishObject.empty_space.value + DishObject.round_rock.value,
       DishObject.round_rock.value + DishObject.empty_space.value
    )
    return section


# Part2
def slide(
    data: List[List[str]],
    direction: Direction
) -> List[List[str]]:
    slided_data = []

    # Only transposing matrix for North and South directions
    if direction in [Direction.north, Direction.south]:
        transposed_data = transpose(l1=data)
    else:
        transposed_data = data

    for row in transposed_data:
        section_string = list_to_string(l1=row)
        sections = section_string.split(DishObject.cube_rock.value)
        new_sections = []

        target_round_rock = DishObject.empty_space.value + DishObject.round_rock.value
        # South and east will move in the opposite direction as north and west
        if direction in [Direction.south, Direction.east]:
            target_round_rock = DishObject.round_rock.value + DishObject.empty_space.value

        for section in sections:
            while target_round_rock in section:
                match direction:
                    case Direction.north:
                        section = move_to_the_left(section=section)
                    case Direction.south:
                        section = move_to_the_right(section=section)
                    case Direction.west:
                        section = move_to_the_left(section=section)
                    case Direction.east:
                        section = move_to_the_right(section=section)

            final_section = DishObject.cube_rock.value
            if section != "":
                final_section = section + DishObject.cube_rock.value

            new_sections += list(final_section)

        # Removing trailing #
        slided_data.append(new_sections[:-1])

    # Only transposing matrix for North and South directions
    if direction in [Direction.north, Direction.south]:
        return transpose(l1=slided_data)
    else:
        return slided_data


def calculate_load(beams: List[List[str]]) -> int:
    load = 0
    current_load = len(beams)
    for row in beams:
        load += row.count(DishObject.round_rock.value) * current_load
        current_load -= 1

    return load


# Part2
def move_to_the_right(section: str):
    # Replacing "O." with ".O" will move one round rock to the right
    section = section.replace(
       DishObject.round_rock.value + DishObject.empty_space.value,
       DishObject.empty_space.value + DishObject.round_rock.value
    )
    return section


def spin_cycle(
    beams: List[List[str]],
    times: int = 1
) -> List[List[str]]:
    copy_beams = []
    east_beams = []
    for num in range(times):
        north_beams = slide(
            data=beams if num == 0 else east_beams,
            direction=Direction.north
        )
        west_beams = slide(data=north_beams, direction=Direction.west)
        south_beams = slide(data=west_beams, direction=Direction.south)
        east_beams = slide(data=south_beams, direction=Direction.east)

        if num == 0:
            copy_beams = copy.deepcopy(north_beams)
        else:
            if copy_beams == north_beams:
                print("Matching original beam matrix after {} times".format(
                    num
                ))
                break
    return east_beams
