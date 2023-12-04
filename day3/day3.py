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

        regex_symbol = "[^\d\n\.]"
        regex_number = "\d+"
        regex_number_before_symbol = "(\d+)(?=[^\d\n\.])"
        regex_number_after_symbol = "(?<=[^\d\n\.])(\d+)"

        symbols_top = re.finditer(regex_symbol, line_top)
        symbols_middle = re.finditer(regex_symbol, line_middle)
        symbols_bottom = re.finditer(regex_symbol, line_bottom)

        # find numbers before and after a symbol adjacent in the same line

        # in-line matches
        before = re.finditer(regex_number_before_symbol, line_top)
        after = re.finditer(regex_number_after_symbol, line_top)
        for match in before:
            part_numbers_dict[line_number_top].add((str(match.start()) + ":" + match.group()))
        for match in after:
            part_numbers_dict[line_number_top].add((str(match.start()) + ":" + match.group()))

        # in-line matches middle line
        before = re.finditer(regex_number_before_symbol, line_middle)
        after = re.finditer(regex_number_after_symbol, line_middle)
        for match in before:
            part_numbers_dict[line_number_top + 1].add((str(match.start()) + ":" + match.group()))
        for match in after:
            part_numbers_dict[line_number_top + 1].add((str(match.start()) + ":" + match.group()))

        # in-line matches middle line
        before = re.finditer(regex_number_before_symbol, line_bottom)
        after = re.finditer(regex_number_after_symbol, line_bottom)
        for match in before:
            part_numbers_dict[line_number_top + 2].add((str(match.start()) + ":" + match.group()))
        for match in after:
            part_numbers_dict[line_number_top + 2].add((str(match.start()) + ":" + match.group()))

        # find symbols in top, middle and bottom line
        # then find numbers in adjacent lines and find out whether symbols are adjacent to any number

        # top line
        for match_symbol in symbols_top:
            # # top compares to middle
            symbol_start = match_symbol.start()
            numbers_middle = re.finditer(regex_number, line_middle)
            part_numbers_dict[line_number_top + 1] = part_numbers_dict[line_number_top + 1].union(
                find_adjacent(numbers_middle, symbol_start))

        # middle line
        for match_symbol in symbols_middle:
            # middle compares to top and bottom
            symbol_start = match_symbol.start()
            numbers_top = re.finditer(regex_number, line_top)
            part_numbers_dict[line_number_top] = part_numbers_dict[line_number_top].union(
                find_adjacent(numbers_top, symbol_start))

            # compare to bottom
            numbers_bottom = re.finditer(regex_number, line_bottom)
            part_numbers_dict[line_number_top + 2] = part_numbers_dict[line_number_top + 2].union(
                find_adjacent(numbers_bottom, symbol_start))

        # bottom line
        for match_symbol in symbols_bottom:
            # bottom compares to middle
            symbol_start = match_symbol.start()
            numbers_middle = re.finditer(regex_number, line_middle)
            part_numbers_dict[line_number_top + 1] = part_numbers_dict[line_number_top + 1].union(
                find_adjacent(numbers_middle, symbol_start))

        line_top = line_middle
        line_middle = line_bottom
        line_number_top += 1


print(part_numbers_dict)

result_dict = 0
for line in part_numbers_dict.values():
    for match in line:
        result_dict += int(match.split(":")[1])

print(result_dict)
