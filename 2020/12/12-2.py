import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')

# Fun logic
ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1

for line in input_str:
    if len(line) == 0:
        continue
    to = line[0]
    num = int(line[1:])
    if to == 'N':
        waypoint_y += num
    elif to == 'S':
        waypoint_y -= num
    elif to == 'E':
        waypoint_x += num
    elif to == 'W':
        waypoint_x -= num
    elif to == 'L' or to == 'R':
        turn = num//90
        if to == 'L':
            turn *= -1
            turn += 4
        if turn == 2:
            waypoint_x *= -1
            waypoint_y *= -1
        elif turn == 1:
            # Right turn, given by:
            # (x')  [ 0 1] (x)
            # (y')  [-1 0] (y)
            waypoint_x, waypoint_y = waypoint_y, waypoint_x * -1
        elif turn == 3:
            # Left turn, given by:
            # (x')  [0 -1] (x)
            # (y')  [1  0] (y)
            waypoint_x, waypoint_y = waypoint_y * -1, waypoint_x
    elif to == 'F':
        ship_x += waypoint_x * num
        ship_y += waypoint_y * num

print(abs(ship_x) + abs(ship_y))

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
