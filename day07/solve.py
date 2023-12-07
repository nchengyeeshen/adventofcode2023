from collections import Counter
import sys

card_strengths = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]

card_strengths_two = [
    "J",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "Q",
    "K",
    "A",
]

hand_strengths = [
    "high_card",
    "one_pair",
    "two_pair",
    "three_of_a_kind",
    "full_house",
    "four_of_a_kind",
    "five_of_a_kind",
]


def hand_type(hand):
    cards = Counter(hand)

    match len(cards):
        case 1:
            return "five_of_a_kind"
        case 2:
            match Counter(cards.values()):
                case {4: 1, 1: 1}:
                    return "four_of_a_kind"
                case {3: 1, 2: 1}:
                    return "full_house"
                case _:
                    raise RuntimeError(f"Unknown hand type: {hand}")
        case 3:
            match Counter(cards.values()):
                case {3: 1, 1: 2}:
                    return "three_of_a_kind"
                case {2: 2, 1: 1}:
                    return "two_pair"
                case _:
                    raise RuntimeError(f"Unknown hand type: {hand}")
        case 4:
            match Counter(cards.values()):
                case {2: 1}:
                    return "one_pair"
                case _:
                    raise RuntimeError(f"Unknown hand type: {hand}")
        case 5:
            return "high_card"
        case _:
            raise RuntimeError(f"Unknown hand type: {hand}")


def hand_type_two(hand):
    cards = Counter(hand)
    num_wildcards = cards.get("J", 0)
    match len(cards):
        case 1:
            return "five_of_a_kind"
        case 2:
            match Counter(cards.values()):
                case {4: 1, 1: 1}:
                    if num_wildcards in [1, 4]:
                        return "five_of_a_kind"
                    return "four_of_a_kind"
                case {3: 1, 2: 1}:
                    if num_wildcards in [2, 3]:
                        return "five_of_a_kind"
                    return "full_house"
                case _:
                    raise RuntimeError(f"Unknown hand type: {hand}")
        case 3:
            match Counter(cards.values()):
                case {3: 1, 1: 2}:
                    if num_wildcards in [1, 3]:
                        return "four_of_a_kind"
                    return "three_of_a_kind"
                case {2: 2, 1: 1}:
                    match num_wildcards:
                        case 2:
                            return "four_of_a_kind"
                        case 1:
                            return "full_house"
                    return "two_pair"
                case _:
                    raise RuntimeError(f"Unknown hand type: {hand}")
        case 4:
            match Counter(cards.values()):
                case {2: 1}:
                    if num_wildcards in [1, 2]:
                        return "three_of_a_kind"
                    return "one_pair"
                case _:
                    raise RuntimeError(f"Unknown hand type: {hand}")
        case 5:
            if num_wildcards == 1:
                return "one_pair"
            return "high_card"
        case _:
            raise RuntimeError(f"Unknown hand type: {hand}")


def part_one(pairs):
    strengths = [
        (
            (
                hand_strengths.index(hand_type(hand)),
                tuple(map(lambda x: card_strengths.index(x), hand)),
            ),
            bid,
        )
        for hand, bid in pairs
    ]
    rankings = sorted(strengths, key=lambda x: x[0])
    return sum((i + 1) * bid for i, (_, bid) in enumerate(rankings))


def part_two(pairs):
    strengths = [
        (
            (
                hand_strengths.index(hand_type_two(hand)),
                tuple(map(lambda x: card_strengths_two.index(x), hand)),
            ),
            bid,
        )
        for hand, bid in pairs
    ]
    rankings = sorted(strengths, key=lambda x: x[0])
    return sum((i + 1) * bid for i, (_, bid) in enumerate(rankings))


if __name__ == "__main__":
    with open("input.txt" if len(sys.argv) < 2 else sys.argv[1]) as f:
        contents = f.read()

    pairs = [
        (hand, int(bid))
        for hand, bid in list(map(lambda x: x.split(), contents.splitlines()))
    ]

    print("Part 1:", part_one(pairs))

    print("Part 2:", part_two(pairs))
