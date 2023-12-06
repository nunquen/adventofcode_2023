import copy
from enum import Enum
from typing import List

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
    day1_input_file = "day_5/input/values.txt"


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
        "rage_legnth": 0
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
        local_range["rage_legnth"] = numbers[2]

        resources[allocate_data].append(copy.deepcopy(local_range))

    return resources


def resource_mapping(resources: List) -> List[dict]:
    entire_map = []
    resource_map = {
        "seed": 0,
        "soil": 0,
        "fertilizer": 0,
        "water": 0,
        "light": 0,
        "temperature": 0,
        "humidity": 0,
        "location": 0
    }
    for seed_to_soil in resources[ResourceRelation.seed_to_soil.value]:
        for num in range(seed_to_soil["rage_legnth"]):
            local_resource_map = copy.deepcopy(resource_map)
            local_resource_map["seed"] = seed_to_soil["source_range_start"] + num
            local_resource_map["soil"] = seed_to_soil["destination_range_start"] + num
            entire_map.append(local_resource_map)

    # Fill the rest of seeds
    # Get max seed
    max_seed = max(resources["seeds"])

    for num in range(max_seed):
        check = list(filter(lambda mapping: mapping["seed"] == num, entire_map))
        if len(check) > 0:
            continue

        local_resource_map = copy.deepcopy(resource_map)
        local_resource_map["seed"] = num
        local_resource_map["soil"] = num
        entire_map.append(local_resource_map)

    # Setting fertilizer
    for soil_to_fertilizer in resources[ResourceRelation.soil_to_fertilizer.value]:
        for num in range(soil_to_fertilizer["rage_legnth"]):
            # Checking if the current soil already exists
            local_resource_map_list = list(
                filter(
                    lambda mapping:
                        mapping["soil"] == soil_to_fertilizer["source_range_start"] + num,
                    entire_map
                    )
                )
            if len(local_resource_map_list) == 0:
                continue

            local_resource_map = local_resource_map_list[0]
            local_resource_map["fertilizer"] = soil_to_fertilizer["destination_range_start"] + num

    return entire_map
