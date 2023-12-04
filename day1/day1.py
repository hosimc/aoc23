import re

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
sum = 0

with open("input.txt", "r") as input:
    for line in input:

        # positive lookahead followed by greed expressing to cover overlapping
        digits = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine)).*(\d|one|two|three|four|five|six|seven|eight|nine)", line)[0]

        # if there's not digits in the line
        if len(digits) == 0:
            continue

        digit1 = ""
        digit2 = ""
        if digits[0].isdigit():
            digit1 = digits[0]
        else:
            digit1 = help_dict[digits[0]]

        if digits[-1].isdigit():
            digit2 = digits[-1]
        else:
            digit2 = help_dict[digits[-1]]

        number = int(digit1 + digit2)
        sum += number

print(sum)