from collections import Counter

input = open("input.txt").read().strip().splitlines()
# input = open("input_demo.txt").read().strip().splitlines()

result = 0

for line in input:
    line = list(map(int, line.split(" ")))
    print(line)
    line.reverse()
    print(line)

    # array for last numbers - already add the last number of current line
    last_numbers = [line[-1]]
    all_zero = False

    while not all_zero:
        sequence = []
        for i in range(1, len(line)):
            sequence.append(line[i] - line[i-1])
        last_numbers.append(sequence[-1])
        line = sequence.copy()
        print(line)
        number_counter = Counter(line)
        if all(element == 0 for element in sequence) or len(line) == 1:
            all_zero = True

    print(last_numbers)
    print(sum(last_numbers))
    result += sum(last_numbers)

print(result)

