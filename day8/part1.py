import math

boxes = [tuple(map(int, x.split(","))) for x in open("day8.txt", "r").read().strip().splitlines()]
n = len(boxes)

def distance(b1, b2):
    return math.sqrt((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2 + (b1[2] - b2[2])**2)

distances = []

for i, b1 in enumerate(boxes):
    for b2 in boxes[i+1:]:
        d = distance(b1, b2)
        distances.append((d, b1, b2))

distances.sort()

circuits = []
connections = {}

for i in range(len(distances)):
    if i >= 1000:
        break

    d, b1, b2 = distances[i]

    if b1 not in connections and b2 not in connections:
        circuits.append({b1, b2})
        connections[b1] = connections[b2] = len(circuits) - 1
    elif b1 in connections and b2 in connections:
        if connections[b1] == connections[b2]:
            continue
        else:
            c1 = connections[b1]
            c2 = connections[b2]
            for b in circuits[c2].copy():
                circuits[c1].add(b)
                circuits[c2].remove(b)
                connections[b] = c1
    elif b1 in connections:
        c = connections[b1]
        circuits[c].add(b2)
        connections[b2] = c
    elif b2 in connections:
        c = connections[b2]
        circuits[c].add(b1)
        connections[b1] = c

lengths = sorted([len(c) for c in circuits], reverse=True)
print(lengths[0] * lengths[1] * lengths[2])

