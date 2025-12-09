tiles = [tuple(map(int, i.split(','))) for i in open("day9.txt", "r").read().splitlines()]

max_area = 0

for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

        if area > max_area:
            max_area = area

print(max_area)
