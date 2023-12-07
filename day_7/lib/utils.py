import copy
from enum import Enum
from typing import Dict, List

debug = False


class LocalFile(Enum):
    day7_input_file = "day_7/input/values.txt"


class Strength(Enum):
    five_of_a_kind = 7   # AAAAA
    four_of_a_kind = 6   # AA8AA
    full_house = 5       # 23332
    three_of_a_kind = 4  # TTT98
    two_pair = 3         # 23432
    one_pair = 2         # A23A4
    high_card = 1        # 23456


class Hand:
    ranks = [
        {"Card": "2", "Value": 1},
        {"Card": "3", "Value": 2},
        {"Card": "4", "Value": 3},
        {"Card": "5", "Value": 4},
        {"Card": "6", "Value": 5},
        {"Card": "7", "Value": 6},
        {"Card": "8", "Value": 7},
        {"Card": "9", "Value": 8},
        {"Card": "T", "Value": 9},
        {"Card": "J", "Value": 10},
        {"Card": "Q", "Value": 11},
        {"Card": "K", "Value": 12},
        {"Card": "A", "Value": 13},
    ]

    def __init__(self, data: str) -> None:
        values = data.split()
        self._cards = values[0]
        self._bet = int(values[1])
        self._strength = Hand.get_hand_strength(hand=self._cards)
        self._numeric_value = self.get_numeric_power()
        self._rank = 0

    @staticmethod
    def get_hand_strength(
        hand: str
    ) -> Strength:
        hand_subset = set(hand)

        if len(hand_subset) == 1:
            return Strength.five_of_a_kind

        if len(hand_subset) == 5:
            return Strength.high_card

        if len(hand_subset) == 4:
            return Strength.one_pair

        if len(hand_subset) == 2:
            if hand.count(list(hand_subset)[0]) == 1 \
                    or hand.count(list(hand_subset)[0]) == 4:
                return Strength.four_of_a_kind
            else:
                return Strength.full_house

        times = 0
        for num in range(len(hand_subset)):
            if hand.count(list(hand_subset)[num]) > times:
                times = hand.count(list(hand_subset)[num])

        if times == 3:
            return Strength.three_of_a_kind

        return Strength.two_pair

    def get_numeric_power(self) -> int:
        power = 0
        base = 10000000000
        for num in range(5):
            card = list(
                filter(
                    lambda x: x["Card"] == self._cards[num], self.ranks
                ))
            power += card[0]["Value"] * base
            base /= 100

        return power


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


def get_hands_from_data(
    source_data: List[str]
) -> List[Hand]:
    hands = []
    for data in source_data:
        hand = Hand(data=data)
        hands.append(hand)

    return hands


def group_hands_by_strength(
    hands: List[Hand]
) -> List:
    grouped_hands = [
        ["Not to be used"], [], [], [], [], [], [], []
    ]
    for hand in hands:
        grouped_hands[hand._strength.value].append(hand)

    return grouped_hands


def sort_and_rank_grouped_hands(
    grouped: List[List]
) -> List[Hand]:
    sorted_and_ranked = []
    global_rank = 1

    for group_hands in grouped:
        if group_hands == ["Not to be used"]:
            continue

        if len(group_hands) == 0:
            continue

        group_hands.sort(key=lambda x: x._numeric_value, reverse=False)
        for card in group_hands:
            card._rank = global_rank
            global_rank += 1
            sorted_and_ranked.append(card)

    return sorted_and_ranked
