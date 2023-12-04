from lib.utils import (
    count_cards_part2,
    get_local_data_as_list,
    LocalFile,
    ScratchCard
)


def test():
    res = True
    test_cards = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]

    cards = []
    value = 0
    for row in test_cards:
        card = ScratchCard(data=row)
        value += card.get_scratchcard_value()
        cards.append(card)

    assert len(cards) == 6
    assert value == 13
    assert count_cards_part2(cards=cards) == 30
    return res


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day1_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)

    value = 0
    cards = []
    for row in input_data:
        card = ScratchCard(data=row)
        value += card.get_scratchcard_value()
        cards.append(card)

    # Part2: count card copies
    value_part2 = count_cards_part2(cards=cards)

    print("Day #4. Get Scratch Cards values part 1. Value: {} ".format(
        value
        )
    )

    print("Day #4. Get Scratch Cards values part 2. Value: {} ".format(
        value_part2
        )
    )
