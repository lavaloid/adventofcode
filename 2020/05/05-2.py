import time

start_time = int(round(time.time() * 1000))

# Input nonsense
f = open("05.txt", "r")
input_str = f.read().split('\n')

# Fun logic
POWER_OF_TWO = [1, 2, 4, 8, 16, 32, 64, 128]

min_id = 1024
max_id = -1
is_seat_empty = [True] * 1024

for seat in input_str:
    if len(seat) == 0:
        continue

    row = 0
    col = 0

    # row
    for i in range(7):
        if seat[i] == 'B':
            row += POWER_OF_TWO[6 - i]

    # column
    for i in range(3):
        if seat[i + 7] == 'R':
            col += POWER_OF_TWO[2 - i]

    seat_id = row * 8 + col
    is_seat_empty[seat_id] = False
    if seat_id < min_id:
        min_id = seat_id
    if seat_id > max_id:
        max_id = seat_id

# now we search for the missing seat id
for i in range(min_id, max_id + 1):
    if is_seat_empty[i]:
        print(i)
        break

end_time = int(round(time.time() * 1000))

print(f"Time: {end_time - start_time} ms")
