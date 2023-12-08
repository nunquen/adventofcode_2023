import copy
from enum import Enum
from typing import Dict, List

debug = False


class LocalFile(Enum):
    day_input_file = "day_8/input/values.txt"


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


def get_nodes_from_data(input_data: str) -> List[dict]:
    output = []

    for data in input_data:
        # Data example -> "AAA = (BBB, CCC)"
        node = {}
        key = data.split("=")[0].strip()
        destination_nodes = data.split("=")[1].strip().\
            replace("(", "").replace(")", "").split(",")

        node[key] = [destination_nodes[0], destination_nodes[1]]
        output.append(node)

    return output
