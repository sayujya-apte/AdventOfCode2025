inp = open("day2.txt", "r").read().split(',')

def is_invalid(s):
    l = len(s)
    for i in range(1, l//2 + 1):
        if l % i == 0:
            pattern = s[:i]
            if pattern * (l // i) == s:
                return True
    return False

for i in range(len(inp)):
    inp[i] = tuple(map(int, inp[i].split('-')))

count = 0
sum = 0

for i in inp:
    for j in range(i[0], i[1]+1):
        if is_invalid(str(j)):
            count += 1
            sum += j

print(count)
print(sum)
