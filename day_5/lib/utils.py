import copy
from enum import Enum
from typing import Dict, List

debug = False


class ResourceRelation(Enum):
    seeds = "seeds"
    seed_to_soil = "seed_to_soil"
    soil_to_fertilizer = "soil_to_fertilizer"
    fertilizer_to_water = "fertilizer_to_water"
    water_to_light = "water_to_light"
    light_to_temperature = "light_to_temperature"
    temperature_to_humidity = "temperature_to_humidity"
    humidity_to_location = "humidity_to_location"


class LocalFile(Enum):
    day5_input_file = "day_5/input/values.txt"


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


def get_seeds(line: str) -> List:
    seeds = []
    if not line.startswith("seeds"):
        return seeds

    seeds = [int(num.strip()) for num in line.split(":")[1].split()]
    return seeds


def get_resource(data: List) -> List:
    local_range = {
        "destination_range_start": 0,
        "source_range_start": 0,
        "range_length": 0
    }
    resources = {
        "seeds": [],
        "seed_to_soil": [],
        "soil_to_fertilizer": [],
        "fertilizer_to_water": [],
        "water_to_light": [],
        "light_to_temperature": [],
        "temperature_to_humidity": [],
        "humidity_to_location": [],
    }

    allocate_data = None

    for line in data:
        if ResourceRelation.seeds.value in line:
            seeds = get_seeds(line=line)
            resources["seeds"] = seeds
            continue

        if line == "":
            allocate_data = None
            continue

        if ResourceRelation.seed_to_soil.value in line:
            allocate_data = ResourceRelation.seed_to_soil.value
            continue

        if ResourceRelation.soil_to_fertilizer.value in line:
            allocate_data = ResourceRelation.soil_to_fertilizer.value
            continue

        if ResourceRelation.fertilizer_to_water.value in line:
            allocate_data = ResourceRelation.fertilizer_to_water.value
            continue

        if ResourceRelation.water_to_light.value in line:
            allocate_data = ResourceRelation.water_to_light.value
            continue

        if ResourceRelation.light_to_temperature.value in line:
            allocate_data = ResourceRelation.light_to_temperature.value
            continue

        if ResourceRelation.temperature_to_humidity.value in line:
            allocate_data = ResourceRelation.temperature_to_humidity.value
            continue

        if ResourceRelation.humidity_to_location.value in line:
            allocate_data = ResourceRelation.humidity_to_location.value
            continue

        numbers = [int(num.strip()) for num in line.split()]
        local_range["destination_range_start"] = numbers[0]
        local_range["source_range_start"] = numbers[1]
        local_range["range_length"] = numbers[2]

        resources[allocate_data].append(copy.deepcopy(local_range))

    return resources


def get_destination_number(
    source_number: int,
    ranges: List[int]
) -> int:
    destination_number = source_number

    for current_range in ranges:
        source_rs = current_range["source_range_start"]
        range_length = current_range["range_length"]
        destination_rs = current_range["destination_range_start"]

        if source_number >= source_rs and\
                source_number <= source_rs + range_length:
            destination_number = source_number - source_rs + destination_rs
            return destination_number

    return destination_number


def mapping(source_data: List) -> List:
    location_paths = []
    location_path = {
        "seed": 0,
        "soil": 0,
        "fertilizer": 0,
        "water": 0,
        "light": 0,
        "temperature": 0,
        "humidity": 0,
        "location": 0,
    }

    for seed in source_data["seeds"]:
        # Get related soil
        soil = get_destination_number(
            source_number=seed,
            ranges=source_data[ResourceRelation.seed_to_soil.value]
        )
        # Get related fertilizer
        fertilizer = get_destination_number(
            source_number=soil,
            ranges=source_data[ResourceRelation.soil_to_fertilizer.value]
        )
        # Get related water
        water = get_destination_number(
            source_number=fertilizer,
            ranges=source_data[ResourceRelation.fertilizer_to_water.value]
        )
        # Get related light
        light = get_destination_number(
            source_number=water,
            ranges=source_data[ResourceRelation.water_to_light.value]
        )
        # Get related temperature
        temperature = get_destination_number(
            source_number=light,
            ranges=source_data[ResourceRelation.light_to_temperature.value]
        )
        # Get related humidity
        humidity = get_destination_number(
            source_number=temperature,
            ranges=source_data[ResourceRelation.temperature_to_humidity.value]
        )
        # Get related location
        location = get_destination_number(
            source_number=humidity,
            ranges=source_data[ResourceRelation.humidity_to_location.value]
        )

        location_path["seed"] = seed
        location_path["soil"] = soil
        location_path["fertilizer"] = fertilizer
        location_path["water"] = water
        location_path["light"] = light
        location_path["temperature"] = temperature
        location_path["humidity"] = humidity
        location_path["location"] = location

        local_location_path = copy.deepcopy(location_path)
        location_paths.append(local_location_path)

    return location_paths


def get_near_location(location_path: List[Dict]) -> int:
    sources = min(location_path, key=lambda x: x["location"])
    return sources["location"]


# Part2
def get_more_seeds(seeds: List[int]) -> List[int]:
    more_seeds = []
    for num in range(0, len(seeds), 2):
        for num2 in range(seeds[num+1]):
            if seeds[num] + num2 not in more_seeds:
                more_seeds.append(seeds[num] + num2)

    return more_seeds
