import re
from collections import defaultdict


def is_adjacent(symbol_start, number_start, number_end):
    if (number_start <= symbol_start <= number_end) or number_start == symbol_start + 1:
        return True


def find_adjacent(numbers, symbol_start):
    results = set()
    for match_number in numbers:
        number_start = match_number.start()
        number_end = match_number.end()
        if (number_start - symbol_start) > 10:
            break
        if is_adjacent(symbol_start, number_start, number_end):
            results.add(str(match_number.start())+":"+match_number.group())
    return results


with open("input.txt", "r") as file:
    line_top = ""
    line_middle = ""
    line_number_top = 0

    part_numbers = set()
    part_numbers_dict = defaultdict(set)

    for line_bottom in file:
        if line_top == "":
            line_top = line_bottom
            continue

        if line_middle == "":
            line_middle = line_bottom
            continue

        regex_symbol = "\*"
        regex_number = "\d+"

        symbols_top = re.finditer(regex_symbol, line_top)
        symbols_middle = re.finditer(regex_symbol, line_middle)
        symbols_bottom = re.finditer(regex_symbol, line_bottom)

        # find asterix (gears) in top, middle and bottom line
        # then find numbers in adjacent lines and find out whether gears are adjacent to any number

        # top line
        for match_symbol in symbols_top:
            symbol_start = match_symbol.start()

            # top compares to top
            numbers = re.finditer(regex_number, line_top)
            part_numbers_dict[str(line_number_top) + ":" + str(symbol_start)] = part_numbers_dict[str(line_number_top) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

            # top compares to middle
            numbers = re.finditer(regex_number, line_middle)
            part_numbers_dict[str(line_number_top) + ":" + str(symbol_start)] = part_numbers_dict[str(line_number_top) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

        # middle line
        for match_symbol in symbols_middle:
            # middle compares to top and bottom
            symbol_start = match_symbol.start()
            numbers = re.finditer(regex_number, line_top)
            part_numbers_dict[str(line_number_top+1) + ":" + str(symbol_start)] = part_numbers_dict[str(line_number_top+1) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

            # middle compares to middle
            numbers = re.finditer(regex_number, line_middle)
            part_numbers_dict[str(line_number_top + 1) + ":" + str(symbol_start)] = part_numbers_dict[
                str(line_number_top + 1) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

            # compare to bottom
            numbers = re.finditer(regex_number, line_bottom)
            part_numbers_dict[str(line_number_top + 1) + ":" + str(symbol_start)] = part_numbers_dict[str(line_number_top + 1) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

        # bottom line
        for match_symbol in symbols_bottom:
            # bottom compares to middle
            symbol_start = match_symbol.start()
            numbers = re.finditer(regex_number, line_middle)
            part_numbers_dict[str(line_number_top + 2) + ":" + str(symbol_start)] = part_numbers_dict[str(line_number_top + 2) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

            # bottom compares to bottom
            numbers = re.finditer(regex_number, line_bottom)
            part_numbers_dict[str(line_number_top + 2) + ":" + str(symbol_start)] = part_numbers_dict[
                str(line_number_top + 2) + ":" + str(symbol_start)].union(
                find_adjacent(numbers, symbol_start))

        line_top = line_middle
        line_middle = line_bottom
        line_number_top += 1

print(part_numbers_dict)

# iterate through found symbols and their adjacent numbers
# multiply numbers where exactly two numbers are adjacent to a symbol
result_dict = 0
for line in part_numbers_dict.values():
    if len(line) == 2:
        gears = []
        for match in line:
            gears.append(int(match.split(":")[1]))
        result_dict += gears[0] * gears[1]

print(result_dict)
