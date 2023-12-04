from collections import Counter
from functools import cache
from sys import argv


def card_score(num: int) -> int:
    if num == 0:
        return 0
    return 2 ** (num - 1)


def card_winning_numbers(card: list[Counter[str]]) -> list[str]:
    winning_numbers, have_numbers = card[0], card[1]
    return [
        num
        for num in have_numbers
        if num in winning_numbers
        and have_numbers[num]
        and have_numbers[num] <= winning_numbers[num]
    ]


def count(cards: list[int]) -> int:
    @cache
    def helper(idx: int) -> int:
        total = 1
        n = cards[idx]
        if n == 0:
            return total
        for i in range(1, n + 1):
            total += helper(idx + i)
        return total

    total = 0
    for idx, _ in enumerate(cards):
        total += helper(idx)
    return total


if __name__ == "__main__":
    filename = argv[1] if len(argv) > 1 else "input.txt"
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()

    cards = [
        [
            Counter(item for item in section.split(" ") if len(item) > 0)
            # 'Card <id>: '
            for section in card[card.index(":") + 2 :].split(" | ")
        ]
        for card in data
    ]

    cards = [len(card_winning_numbers(card)) for card in cards]

    # Part 1
    print("Total points:", sum(card_score(card) for card in cards))

    # Part 2
    print("Total scratch cards:", count(cards))
