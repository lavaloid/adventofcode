import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')

# Fun logic
x_pos = 0
y_pos = 0
facing = 0
# 0 = east
# 1 = south
# 2 = west
# 3 = north

for line in input_str:
    if len(line) == 0:
        continue
    to = line[0]
    num = int(line[1:])
    if to == 'N':
        y_pos += num
    elif to == 'S':
        y_pos -= num
    elif to == 'E':
        x_pos += num
    elif to == 'W':
        x_pos -= num
    elif to == 'L':
        facing -= num//90
        if facing < 0:
            facing += 4
    elif to == 'R':
        facing += num//90
        if facing >= 4:
            facing -= 4
    elif to == 'F':
        if facing == 0:
            x_pos += num
        elif facing == 1:
            y_pos -= num
        elif facing == 2:
            x_pos -= num
        elif facing == 3:
            y_pos += num

print(abs(x_pos) + abs(y_pos))

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
