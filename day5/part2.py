parts = open("day5.txt", "r").read().strip().split("\n\n")

ranges = parts[0].strip().split('\n')
for i in range(len(ranges)):
    ranges[i] = tuple(map(int, ranges[i].split('-')))

sorted_ranges = sorted(ranges, key = lambda x : x[0])

current_low, current_high = sorted_ranges[0]
total = 0

for next_low, next_high in sorted_ranges[1:]:
    if next_low <= current_high:
        current_high = max(current_high, next_high)
    else:
        total += current_high - current_low + 1
        current_low, current_high = next_low, next_high

total += current_high - current_low + 1

print(total)

