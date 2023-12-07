from collections import Counter
strengths = {"T": 10,
             "J": 11,
             "Q": 12,
             "K": 13,
             "A": 14}


def card_value(char):
    if char in strengths:
        return strengths[char] + 26
    if not char.isalpha():
        return int(char)
    return ord(char)


input = open("input.txt").read().strip().splitlines()
hands = {key_value.split(" ")[0]: key_value.split(" ")[1] for key_value in input}
print(hands)

# five of a kind
# four of a kind
# full house - 3 + 2
# three of a kind
# two pair
# one pair
# high card

hand_types = {"five": [],
              "four": [],
              "full": [],
              "three": [],
              "two2": [],
              "2": [],
              "1": []}

for hand in hands:
    hand_cards = {}
    for card in hand:
        hand_cards[card] = hand_cards.get(card, 0) + 1
    print(hand_cards)

    hand_dict = (hand, hands.get(hand))

    if 5 in hand_cards.values():
        hand_types["five"].append(hand_dict)
        continue
    if 4 in hand_cards.values():
        hand_types["four"].append(hand_dict)
        continue
    if 3 in hand_cards.values() and 2 in hand_cards.values():
        hand_types["full"].append(hand_dict)
        continue
    if 3 in hand_cards.values():
        hand_types["three"].append(hand_dict)
        continue
    if 2 in hand_cards.values():
        value_counter = Counter(hand_cards.values())
        if value_counter.get(2, 0) == 1:
            hand_types["2"].append(hand_dict)
        elif value_counter.get(2, 0) == 2:
            hand_types["two2"].append(hand_dict)
        continue
    else:
        hand_types["1"].append(hand_dict)

print(hand_types)

result_list = []

for hand_type in hand_types:
    sorted_list = sorted(hand_types.get(hand_type), key=lambda s: [card_value(char) for char in s[0]], reverse=True)
    print(sorted_list)
    for item in sorted_list:
        result_list.append(item[1])

print(result_list)

result = 0
for i in range(len(result_list)):
    result += int(result_list[i])*(len(result_list)-i)

print(result)

