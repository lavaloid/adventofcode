import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("input.txt", "r")
input_str = f.read().split('\n')
input_str.pop()

# Fun logic
seats = []
for input_row in input_str:
    seat_row = []
    for input_col in input_row:
        seat_row.append(input_col)
    seats.append(seat_row)

WIDTH = len(seats[0])
HEIGHT = len(seats)

def is_pos_valid(x, y):
    if x < 0 or x >= WIDTH:
        return False

    if y < 0 or y >= HEIGHT:
        return False

    return True

def count_occupied(x ,y):
    result = 0

    adj = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for d in adj:
        new_x = x + d[0]
        new_y = y + d[1]
        if is_pos_valid(new_x, new_y):
            if seats[new_y][new_x] == '#':
                result += 1

    return result

seat_change = [[0] * WIDTH for k in range(HEIGHT)]
change_count = -1
while change_count != 0:
    change_count = 0
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if seats[j][i] == '.':
                continue

            occ = count_occupied(i, j)
            if occ == 0 and seats[j][i] == 'L':
                seat_change[j][i] = 1
                change_count += 1
            elif occ >= 4 and seats[j][i] == '#':
                seat_change[j][i] = 1
                change_count += 1
    
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if seat_change[j][i] == 1:
                seat_change[j][i] = 0
                if seats[j][i] == 'L':
                    seats[j][i] = '#'
                elif seats[j][i] == '#':
                    seats[j][i] = 'L'

total = 0
for i in range(WIDTH):
    for j in range(HEIGHT):
        if seats[j][i] == '#':
            total += 1

print(total)

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
