from lib.utils import (
    get_local_data_as_list,
    get_hands_from_data,
    group_hands_by_strength,
    sort_and_rank_grouped_hands,
    LocalFile,
    Hand
)

'''
Reference: https://adventofcode.com/2023/day/7
'''


def test():
    data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    hands = get_hands_from_data(source_data=data)
    group_hands = group_hands_by_strength(hands=hands)
    sorted = sort_and_rank_grouped_hands(grouped=group_hands)
    total_winnings = 0
    for card in sorted:
        total_winnings += (card._bet * card._rank)

    assert total_winnings == 6440

    # Part2: Use Joker
    group_hands = group_hands_by_strength(hands=hands, use_joker=True)
    sorted = sort_and_rank_grouped_hands(grouped=group_hands, use_joker=True)
    total_winnings_with_joker = 0
    for card in sorted:
        total_winnings_with_joker += (card._bet * card._rank)

    return total_winnings_with_joker == 5905


if __name__ == "__main__":

    if not test():
        exit(1)

    input_file = LocalFile.day7_input_file.value
    input_data = get_local_data_as_list(input_file=input_file)

    hands = get_hands_from_data(source_data=input_data)
    group_hands = group_hands_by_strength(hands=hands)
    sorted = sort_and_rank_grouped_hands(grouped=group_hands)
    total_winnings = 0
    for card in sorted:
        total_winnings += (card._bet * card._rank)

    print("Day #7. Total winning Part1. Value: {} ".format(
        total_winnings
        )
    )

    # Part2: Use Joker
    group_hands = group_hands_by_strength(hands=hands, use_joker=True)
    sorted = sort_and_rank_grouped_hands(grouped=group_hands, use_joker=True)
    total_winnings_with_joker = 0
    for card in sorted:
        total_winnings_with_joker += (card._bet * card._rank)

    print("Day #7. Total winning Part2. Value: {} ".format(
        total_winnings_with_joker
        )
    )

    for card in sorted:
        print("{} - {}".format(card._cards, card._joker_cards))
