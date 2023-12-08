from math import lcm

# LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
#
# AAA -> BBB (L) -> AAA (L) -> BBB (R) -> AAA (L) -> BBB (L) -> ZZZ(R)

input = open("input.txt").read().strip().splitlines()
direction = input[0]
nodes = {}
nodesA = []

for i in range(2, len(input)):
    line = input[i]
    node_name = line.split("=")[0][:-1]
    dirL = line.split("=")[1].split(",")[0][2:]
    dirR = line.split("=")[1].split(",")[1][1:-1]
    nodes[node_name] = (dirL, dirR)
    if node_name[-1] == "A":
        nodesA.append(node_name)

direction = direction.replace("L", "0").replace("R", "1")
print(direction)

nodeB = ""
steps = 0
steps_list = []

# get required steps for every node
while len(nodesA) > 0:
    for side in direction:
        steps += 1
        nodesA_copy = nodesA.copy()
        for nodeA in nodesA_copy:
            nodeB = nodes[nodeA][int(side)]
            if nodeB[-1] == "Z":
                nodesA.pop(nodesA.index(nodeA))
                steps_list.append(steps)
                continue
            nodesA[nodesA.index(nodeA)] = nodeB

print(steps_list)

# LCM of all results
result = steps_list[0]
for step in steps_list[1:]:
    result = lcm(result, step)

print(result)
