import sys
from collections import Counter


def card_score(winning_numbers):
    n = len(winning_numbers)
    if n == 0:
        return 0
    return 2 ** (n - 1)


def card_winning_numbers(card):
    winning_numbers, have_numbers = card[0], card[1]
    return [
        num
        for num in have_numbers
        if num in winning_numbers
        and have_numbers[num]
        and have_numbers[num] <= winning_numbers[num]
    ]


def count(cards):
    total = 0
    for idx, _ in enumerate(cards):
        total += count_aux(cards, idx)
    return total


def count_aux(cards, idx):
    total = 1
    n = len(cards[idx])
    if n == 0:
        return total
    for i in range(1, n + 1):
        total += count_aux(cards, idx + i)
    return total


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        data = f.read().strip().splitlines()

    cards = [
        [
            Counter(item for item in section.split(" ") if len(item) > 0)
            for section in card[card.index(":") + 2 :].split(" | ")
        ]
        for card in data
    ]

    cards = [card_winning_numbers(card) for card in cards]

    # Part 1
    print("Total points:", sum(card_score(card) for card in cards))

    # Part 2
    print("Total scratch cards:", count(cards))
