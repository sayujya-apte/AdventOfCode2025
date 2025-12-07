data = open("day6.txt", "r").read().strip().split('\n')

operators = data[-1].split()
operands = []

for i in range(len(data)-1):
    s = data[i].split()
    lst = list(map(int, s))
    operands.append(lst)

res = 0

for i in range(len(operators)):
    if operators[i] == '+':
        a = 0
        for j in operands:
            a += j[i]
        res += a
    elif operators[i] == '*':
        a = 1
        for j in operands:
            a *= j[i]
        res += a

print(res)
