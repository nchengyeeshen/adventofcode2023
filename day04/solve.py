from collections import Counter
import sys

data = sys.stdin.read().strip().splitlines()

cards = []
for card in data:
    card = card[card.index(":") + 2 :]
    sections = card.split(" | ")
    parts = []
    for section in sections:
        items = []
        for item in section.split(" "):
            if len(item) == 0:
                continue
            items.append(item)
        parts.append(items)
    cards.append(parts)

total_points = 0
for card in cards:
    winning_numbers = Counter(card[0])
    have_numbers = Counter(card[1])

    matching = 0
    for num in have_numbers:
        if num in winning_numbers and have_numbers[num] <= winning_numbers[num]:
            matching += 1
    if matching >= 1:
        total_points += 2 ** (matching - 1)

print("Total points:", total_points)
