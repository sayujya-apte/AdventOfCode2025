shelves = open("day4.txt", "r").read().strip().split('\n')

total = 0

row_count = len(shelves)
col_count = len(shelves[0])

def get_neighbours(r, c):
    neighbours = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < row_count and 0 <= nc < col_count:
                neighbours.append((nr, nc))
    return neighbours

shelves = [list(row) for row in shelves]

while True:
    to_remove = []
    for row in range(len(shelves)):
        for col in range(len(shelves[row])):
            if shelves[row][col] == "@":
                neighbours = get_neighbours(row, col)
                neighbour_count = 0
                for neighbour in neighbours:
                    if shelves[neighbour[0]][neighbour[1]] == "@":
                        neighbour_count += 1
                if neighbour_count < 4:
                    to_remove.append((row, col))

    if not to_remove:
        break

    for row, col in to_remove:
        shelves[row][col] = "."

    total += len(to_remove)

print(total)
