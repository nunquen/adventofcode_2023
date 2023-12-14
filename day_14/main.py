from lib.utils import (
    get_local_data_as_list,
    LocalFile,
    Direction,
    current_day,
    prepare_data,
    slide,
    calculate_load,
    spin_cycle,
)

'''
--- Day 14: Haunted Wasteland ---
Reference: https://adventofcode.com/2023/day/14
'''


def test():
    input_data = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]

    data = prepare_data(data=input_data)

    slided_data = slide(
        data=data,
        direction=Direction.north
    )

    total_load = calculate_load(beams=slided_data)

    assert total_load == 136

    return True


if __name__ == "__main__":

    if not test():
        exit(1)

    print("Day {}. Tests passed!".format(current_day))

    print("Day {} Part1".format(current_day))
    input_file = LocalFile.day_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)

    print("  Preparing data")
    data = prepare_data(data=input_data)
    print("  Moving round objects to north")
    slided_data = slide(
        data=data,
        direction=Direction.north
    )
    print("  Calculating loads")
    total_load = calculate_load(beams=slided_data)
    print("  Current load is: {}".format(total_load))

    print("Day {} Part2".format(current_day))
    cycles = 1000000000
    print("  Spinning cycles: {}".format(cycles))
    spinned_data = spin_cycle(
            beams=data,
            times=cycles
        )
    print("  Moving round objects to north")
    slided_data = slide(
        data=spinned_data,
        direction=Direction.north
    )
    print(">>> East beams after {} cycles:\n{}".format(cycles, slided_data))
    print("  Calculating loads")
    total_load = calculate_load(beams=slided_data)
    print("  Loads: {}".format(total_load))

    print(">>> North beams:\n{}".format(slided_data))
    print("  Calculating loads")
    total_load = calculate_load(beams=slided_data)
    print("  Loads: {}".format(total_load))
