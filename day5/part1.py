parts = open("day5.txt", "r").read().strip().split("\n\n")

ranges = parts[0].strip().split('\n')
for i in range(len(ranges)):
    ranges[i] = tuple(map(int, ranges[i].split('-')))

ings = list(map(int, parts[1].strip().split('\n')))

count = 0

for i in ings:
    for low, high in ranges:
        if low <= i <= high:
            count += 1
            break

print(count)
