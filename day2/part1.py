inp = open("day2.txt", "r").read().split(',')

for i in range(len(inp)):
    inp[i] = tuple(map(int, inp[i].split('-')))

count = 0
sum = 0

for i in inp:
    for j in range(i[0], i[1]+1):
        j_str = str(j)
        left = j_str[:len(j_str)//2]
        right = j_str[len(j_str)//2:]
        if left == right:
            count += 1
            sum += j

print(count)
print(sum)
