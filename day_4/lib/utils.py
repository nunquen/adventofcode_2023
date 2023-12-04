from enum import Enum
from typing import List

debug = False


class LocalFile(Enum):
    day1_input_file = "day_4/input/values.txt"


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


class ScratchCard:
    def __init__(
        self,
        data: str
    ) -> None:
        self._number = int(data.split(":")[0].replace("Card", "").strip())
        self._winning_numbers = ScratchCard.get_numbers_from_string(
            phrase=data.split(":")[1].split("|")[0]
        )
        self._my_numbers = ScratchCard.get_numbers_from_string(
            phrase=data.split(":")[1].split("|")[1]
        )
        # Part2
        self._my_winning_numbers = 0
        self._instances = 1

    @staticmethod
    def get_numbers_from_string(phrase: str) -> List:
        numbers = [int(num.strip()) for num in phrase.split()]
        return numbers

    def get_scratchcard_value(self) -> int:
        value = 0
        my_winning_numbers = set(self._my_numbers) & set(self._winning_numbers)
        if len(my_winning_numbers) == 0:
            return value

        value = pow(2, len(my_winning_numbers) - 1)

        # Part2
        self._my_winning_numbers = len(my_winning_numbers)
        return value

    def get_my_winning_numbers(self) -> int:
        return self._my_winning_numbers

    def add_copy(self):
        self._instances += 1

    def get_instances(self) -> int:
        return self._instances


def count_cards_part2(cards: List) -> int:
    total_scratchcards = 0
    for pos1 in range(len(cards)):
        if pos1 == len(cards) - 1:
            continue

        numbers = cards[pos1].get_my_winning_numbers()
        if numbers == 0:
            continue

        max_position = (pos1 + numbers + 1 if pos1 + numbers <= len(cards) - 1 else len(cards))
        for times in range(cards[pos1].get_instances()):
            for pos2 in range(
                pos1 + 1,
                max_position
            ):
                cards[pos2].add_copy()

    for pos1 in range(len(cards)):
        total_scratchcards += cards[pos1].get_instances()

    return total_scratchcards
