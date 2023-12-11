from lib.utils import (
    get_local_data_as_list,
    get_nodes_from_data,
    LocalFile,
    Direction,
)

'''
--- Day 8: Haunted Wasteland ---
Reference: https://adventofcode.com/2023/day/8
'''


def test():
    directions = "RL"
    input_data = [
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    nodes = get_nodes_from_data(input_data=input_data)

    direction = Direction(
        directions=directions,
        nodes=nodes
        )

    steps = direction.get_steps()
    assert steps == 2

    input_data = [
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    nodes = get_nodes_from_data(input_data=input_data)
    direction = Direction(
        directions="LLR",
        nodes=nodes
        )
    steps = direction.get_steps()
    assert steps == 6
    return True


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)
    directions = input_data[0]
    input_data = input_data[2:]
    nodes = get_nodes_from_data(input_data=input_data)

    direction = Direction(
        directions=directions,
        nodes=nodes
        )

    steps = direction.get_steps()
    print("Day 8. Steps to reach destination. Part1. Value: {} ".format(
        steps
        )
    )
