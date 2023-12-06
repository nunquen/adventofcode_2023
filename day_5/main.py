from lib.utils import (
    get_resource,
    get_local_data_as_list,
    LocalFile,
    resource_mapping,
)

'''
Reference: https://adventofcode.com/2023/day/5
'''


def test():
    res = True
    data = [
        "seeds: 79 14 55 13",
        "seed_to_soil map:",
        "50 98 2",
        "52 50 48",
        "soil_to_fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "fertilizer_to_water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "water_to_light map:",
        "88 18 7",
        "18 25 70",
        "light_to_temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "temperature_to_humidity map:",
        "0 69 1",
        "1 0 69",
        "humidity_to_location map:",
        "60 56 37",
        "56 93 4",
    ]
    resources = get_resource(data=data)
    assert len(resources["seeds"]) == 4
 
    rm = resource_mapping(resources=resources)
    return res


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day1_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)

    print("Day #5. Get Scratch Cards values part 1. Value: {} ".format(
        None
        )
    )
