from lib.utils import (
    get_local_data_as_list,
    get_near_location,
    get_resource,
    LocalFile,
    mapping,
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
    resouces_mapped = mapping(source_data=resources)
    assert resouces_mapped[0]["seed"] == 79
    assert resouces_mapped[0]["location"] == 82

    # Get nearest location
    near_location = get_near_location(location_path=resouces_mapped)
    assert near_location == 35
    return near_location == 35


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day5_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)
    resources = get_resource(data=input_data)
    resouces_mapped = mapping(source_data=resources)
    # Get nearest location
    near_location = get_near_location(location_path=resouces_mapped)

    print("Day #5. Get Near location Value: {} ".format(
        near_location
        )
    )
