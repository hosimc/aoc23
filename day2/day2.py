import re

red = 12
green = 13
blue = 14

result = 0
power = 0

with open("input.txt", "r") as file:
    for line in file:
        game = re.findall("(?<=Game\s)[\d]+", line)
        reds = list(map(int, re.findall("(?:(\d+))\s(?:red)", line)))
        blues = list(map(int, re.findall("(?:(\d+))\s(?:blue)", line)))
        greens = list(map(int, re.findall("(?:(\d+))\s(?:green)", line)))

        reds.sort()
        blues.sort()
        greens.sort()

        if len(game) > 0:
            game = int(game[0])

        power += reds[-1] * blues[-1] * greens[-1]

        if int(reds[-1]) > red or int(blues[-1]) > blue or int(greens[-1]) > green:
            continue

        result += game

print(result)
print(power)