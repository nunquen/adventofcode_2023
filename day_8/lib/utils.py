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
    output_data = {}

    for data in input_data:
        """
        input_data = [
            "AAA = (BBB, CCC)",
            "BBB = (DDD, GGG)"
        ]
        output_data = {
            "AAA": ["BBB", "CCC"],
            "BBB": ["DDD", "GGG"],
        }
        """
        key = data.split("=")[0].strip()
        destination_nodes = data.split("=")[1].strip().\
            replace("(", "").replace(")", "").split(",")

        output_data[key] = [destination_nodes[0].strip(), destination_nodes[1].strip()]

    return output_data


class Direction:
    def __init__(
        self,
        directions: str,
        nodes: List[dict]
    ) -> None:
        self._directions = []
        self._current_position = 0
        for direction in directions:
            self._directions.append(direction)
        self._last_direction = self._directions[-1:][0]
        self._nodes = nodes
        self._origin = "AAA"
        self._destination = "ZZZ"

    def get_direction(self):
        direction = None
        if self._current_position < len(self._directions):
            direction = self._directions[self._current_position]

        self._current_position += 1

        return direction

    def get_node(self, name: str) -> Dict:
        try:
            return self._nodes[name]
        except Exception as e:
            print("FATAL ERROR. Node nam {} does not exists!\n{}".format(
                name,
                str(e)
            ))
            exit(1)

    def get_steps(self) -> int:
        steps = 1
        # Starting with node AAA
        current_node_name = self._origin
        found = False

        for num in range(len(self._directions)):
            node = self.get_node(current_node_name)
            direction = self.get_direction()
            next_node_name = node[0] if direction == "L" else node[1]
            if next_node_name == self._destination:
                found = True
                break

            current_node_name = next_node_name

        steps += num

        if found:
            return steps

        # Searching with LRLRLRLRLRLRLRLRL.....
        current_node_name = self._origin
        in_loop = True
        direction = "L"
        steps += 1
        path = []
        iterator = 0
        while in_loop:
            node = self.get_node(current_node_name)

            path.append(
                {
                    "node": current_node_name,
                    "direction": direction,
                    "index": iterator
                }
            )
            next_node_name = node[0] if direction == "L" else node[1]

            # is_next_node_revisited = list(
            #     filter(
            #         lambda x: x["node"] == next_node_name,
            #         path
            #     )
            # )

            # if len(is_next_node_revisited) > 0:
            #     # Lets go to the other direction
            #     direction = "L" if is_next_node_revisited["direction"] == "R" else "R"
            #     next_node_name = node[0] if direction == "L" else node[1]

            steps += 1

            if next_node_name == self._destination:
                in_loop = False
                break

            current_node_name = next_node_name
            direction = "R" if direction == "L" else "L"

        return steps
