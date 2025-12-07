inputs = open("day1.txt", "r").read().split('\n')[:-1]

state = 50
count = 0

def rotate(state, direction, distance):
    if direction == 'L':
        return (state - distance) % 100
    elif direction == 'R':
        return (state + distance) % 100

for i in inputs:
    direction = i[0]
    distance = int(i[1:])
    state = rotate(state, direction, distance)
    if state == 0:
        count += 1

print("state = ", state)
print("count = ", count)
