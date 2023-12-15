import copy
from enum import Enum
from typing import List


debug = False
current_day = 15


class Operation(Enum):
    remove = "-"
    add = "="


class LocalFile(Enum):
    day_input_file = "day_{}/input/values.txt".format(current_day)


def get_local_data_as_list(input_file: str) -> List:
    content = []
    try:
        local_file = open(input_file, "r")
        for line in local_file.readlines():
            content = line.rstrip("\n").split(",")
            break
    except Exception as e:
        print("Error while reading file {}. The error:\n{}".format(
            input_file,
            str(e)
        ))

    return content


def hash_algorithm(phrase: str) -> int:
    value = 0
    multiplier = 17
    divider = 256

    for letter in phrase:
        value += ord(letter)
        value = (value * multiplier) % divider

    return value


def get_values(phrases: List[str]) -> int:
    value = 0
    for phrase in phrases:
        value += hash_algorithm(phrase=phrase)

    return value


def get_boxes() -> List[dict]:
    boxes = []
    box = {
        "name": "Box #",
        "number": 0,
        "lenses": []
    }

    for num in range(256):
        b = copy.deepcopy(box)
        b["name"] = b["name"].replace("#", str(num))
        b["number"] = num
        boxes.append(b)

    return boxes


# Part 2
def hashmap(input_data: List[str]) -> List[dict]:
    boxes = get_boxes()

    for label in input_data:
        remove_lens = True if Operation.remove.value in label else False

        if remove_lens:
            for box in boxes:
                current_lens = list(filter(
                    lambda x:
                    label[:-1] in x,
                    box["lenses"]
                ))

                if len(current_lens) == 0:
                    continue

                for num in reversed(range(len(box["lenses"]))):
                    if box["lenses"][num] in current_lens:
                        box["lenses"].pop(num)

            continue

        # Adding label
        this_label = label.split(Operation.add.value)[0]
        hash_value = hash_algorithm(phrase=this_label)
        current_lens = list(filter(
                    lambda x:
                    this_label in x,
                    boxes[hash_value]["lenses"]
                ))

        if len(current_lens) == 0:
            # No lens like this one in the box
            boxes[hash_value]["lenses"].append(label.replace(
                Operation.add.value, " "
            ))
        else:
            # The lens is present in the box
            position = boxes[hash_value]["lenses"].index(
                current_lens[0]
            )
            # Replacing old lens with new one
            boxes[hash_value]["lenses"][position] = label.replace(
                Operation.add.value, " "
                )

    return boxes


def focusing_power(boxes: List[dict]) -> int:
    power = 0

    for box_index in range(len(boxes)):
        box = boxes[box_index]
        one_plus = box_index + 1
        if len(box["lenses"]) == 0:
            continue

        for num in range(len(box["lenses"])):
            slot_number = num + 1
            focal_length = int(box["lenses"][num].split()[1])
            power += one_plus * slot_number * focal_length

    return power
