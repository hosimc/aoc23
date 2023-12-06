import re
from math import ceil

# Time:      7  15   30
# Distance:  9  40  200


def possible_solutions(race_time, race_distance):
    b = race_time
    c = race_distance

    # Calculate discriminant
    delta = b ** 2 - 4 * c

    root1 = ceil(((b + delta ** 0.5) / 2))
    root2 = ceil(((b - delta ** 0.5) / 2))

    # Print the solution for the inequality
    return root1 - root2


def part1(file):
    with open("input.txt", "r") as file_o:
        lines = file_o.readlines()
        times = re.findall("\d+", lines[0])
        distances = re.findall("\d+", lines[1])

        result = 1
        result_fun = 1

        for i in range(len(times)):
            possibilities = 0
            time = int(times[i])
            distance = int(distances[i])
            print("function solution: " + str(possible_solutions(time, distance)))
            result_fun *= possible_solutions(time, distance)
        print("function result: " + str(result_fun))
        file_o.close()


def part2(file):
    with open("input.txt", "r") as file_o:
        lines = file_o.readlines()
        times = re.findall("\d+", lines[0])
        distances = re.findall("\d+", lines[1])

        result = 0
        time = int("".join(times))
        distance = int("".join(distances))

        print(time)
        print(distance)

        print("function solution: " + str(possible_solutions(time, distance)))
        file_o.close()


filename = "input.txt"
print("part 1")
part1(filename)

print()
print("part 2")
part2(filename)
