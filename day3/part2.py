banks = open("day3.txt", "r").read().strip().split('\n')

sum = 0

def largest_joltage(bank, k):
    n = len(bank)
    pos = 0
    batteries = []

    for remaining in range(k, 0, -1):
        end = n - remaining + 1
        best_digit = max(bank[pos:end])
        pos = bank.index(best_digit, pos, end) + 1
        batteries.append(best_digit)
    
    return ''.join(batteries)

for bank in banks:
    sum += int(largest_joltage(bank, 12))

print(sum)
