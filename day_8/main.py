from lib.utils import (
    get_local_data_as_list,
    get_nodes_from_data,
    LocalFile,
)

'''
--- Day 8: Haunted Wasteland ---
Reference: https://adventofcode.com/2023/day/8
'''


def test():
    input_data = [
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    data = get_nodes_from_data(input_data=input_data)

    assert len(data) == 0
    return True


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)

    print("Day 8. Spets to reach destination. Part1. Value: {} ".format(
        None
        )
    )
