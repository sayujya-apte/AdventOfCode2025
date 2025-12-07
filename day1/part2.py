inputs = open("day1.txt", "r").read().split('\n')[:-1]

state = 50
count = 0

def rotate(state, direction, distance):
    if direction == 'L':
        zeroes = ((state-1) // 100) - ((state - distance - 1) // 100)
        return (state - distance) % 100, zeroes
    elif direction == 'R':
        zeroes = ((state + distance) // 100) - ((state) // 100)
        return (state + distance) % 100, zeroes

for i in inputs:
    direction = i[0]
    distance = int(i[1:])
    state, zeroes = rotate(state, direction, distance)
    count += zeroes

print("state = ", state)
print("count = ", count)
