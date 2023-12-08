
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

for i in range(2, len(input)):
    line = input[i]
    node_name = line.split("=")[0][:-1]
    dirL = line.split("=")[1].split(",")[0][2:]
    dirR = line.split("=")[1].split(",")[1][1:-1]
    nodes[node_name] = (dirL, dirR)

direction = direction.replace("L", "0").replace("R", "1")
print(direction)

nodeA = nodes["AAA"]
nodeB = ""

steps = 0
while nodeB != "ZZZ":
    for side in direction:
        steps += 1
        print(nodeA)
        nodeB = nodeA[int(side)]
        if nodeB == "ZZZ":
            break
        print(nodeB)
        nodeA = nodes[nodeB]

print(steps)