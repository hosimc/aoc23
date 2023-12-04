import re

# sample input
# Card   1: 33 56 23 64 92 86 94  7 59 13 | 86 92 64 43 10 70 16 55 79 33 56  8  7 25 82 14 31 96 94 13 99 29 69 75 23

# demo
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

# 1, 11
index_winning = 1
index_my_numbers = 11

cards = {}

with open("input.txt", "r") as file:
    for line in file:
        numbers = re.findall("(?<=\s)\d+", line)
        card_number = int(numbers[0])

        # first time on this card, add it to the cards dict
        if card_number not in cards:
            cards[card_number] = 1
        else:
            cards[card_number] += 1

        for i in range(cards[card_number]):
            winning_numbers = numbers[index_winning:index_my_numbers]
            my_numbers = numbers[index_my_numbers:len(numbers)]

            card_value = 0
            for number in my_numbers:
                if number in winning_numbers:
                    card_value += 1

            while card_value > 0:
                if (card_number + card_value) in cards:
                    cards[card_number + card_value] += 1
                else:
                    cards[card_number + card_value] = 1
                card_value -= 1

# print(cards)
print(sum(cards.values()))
