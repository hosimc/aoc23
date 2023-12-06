import re

# Time:      7  15   30
# Distance:  9  40  200


def possible_solutions(race_time, race_distance):
    a = 1
    b = race_time
    c = race_distance

    # Calculate discriminant
    delta = b ** 2 - 4 * a * c

    root1 = round(((b + delta ** 0.5) / (2 * a)).real)
    root2 = round(((b - delta ** 0.5) / (2 * a)).real)

    # Print the solution for the inequality
    return root1 - root2 + 1


def part1(file):
    with open("input.txt", "r") as file_o:
        lines = file_o.readlines()
        times = re.findall("\d+", lines[0])
        distances = re.findall("\d+", lines[1])

        result = 1

        for i in range(len(times)):
            possibilities = 0
            time = int(times[i])
            distance = int(distances[i])
            for i in range(time):
                if i * (time - i) > distance:
                    possibilities += 1
            print(possibilities)
            result *= possibilities

        print("result = " + str(result))
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

        for i in range(time):
            if i * (time - i) > distance:
                result += 1

        print("result = " + str(result))
        file_o.close()


filename = "input.txt"
print("part 1")
part1(filename)

print()
print("part 2")
part2(filename)
